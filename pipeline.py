"""Calcul de la marge journalière par commodity -> output/margin_daily.csv."""
from pathlib import Path

import pandas as pd

from config import OUTPUT_CSV, PRICES_CSV, TRADES_CSV


def compute_margin(trades: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, t in trades.iterrows():
        if t.status == "CANCELLED":
            continue
        p = prices[(prices.price_date == t.trade_date) & (prices.commodity == t.commodity)]
        for _, m in p.iterrows():
            sign = 1 if t.side == "SELL" else -1
            margin = sign * (t.price_eur_mwh - m.price_eur_mwh) * t.volume_mwh - t.fee_eur
            rows.append((t.trade_date, t.commodity, margin))
    df = pd.DataFrame(rows, columns=["trade_date", "commodity", "margin_eur"])
    return df.groupby(["trade_date", "commodity"], as_index=False).margin_eur.sum()


def run():
    trades = pd.read_csv(TRADES_CSV, parse_dates=["trade_date"])
    prices = pd.read_csv(PRICES_CSV, parse_dates=["price_date", "loaded_at"])
    out = compute_margin(trades, prices)
    Path(OUTPUT_CSV).parent.mkdir(exist_ok=True)
    out.to_csv(OUTPUT_CSV, index=False)
    print(OUTPUT_CSV, ":", len(out), "lignes")


if __name__ == "__main__":
    run()
