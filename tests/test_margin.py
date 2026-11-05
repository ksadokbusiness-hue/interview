import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline import compute_margin

D = pd.Timestamp("2026-09-01")
PRICES = pd.DataFrame({"price_date": [D], "commodity": ["GAS_TTF"], "price_eur_mwh": [40.0]})


def trade(side, status="CONFIRMED"):
    return pd.DataFrame([dict(trade_date=D, commodity="GAS_TTF", side=side, status=status,
                              volume_mwh=100, price_eur_mwh=42.0, fee_eur=2.0)])


class TestMargin(unittest.TestCase):
    def test_sell(self):
        self.assertEqual(compute_margin(trade("SELL"), PRICES).margin_eur[0], 198.0)

    def test_buy(self):
        self.assertEqual(compute_margin(trade("BUY"), PRICES).margin_eur[0], -202.0)

    def test_cancelled_ignored(self):
        self.assertTrue(compute_margin(trade("SELL", "CANCELLED"), PRICES).empty)


if __name__ == "__main__":
    unittest.main()
