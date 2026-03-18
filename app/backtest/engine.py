import pandas as pd


class BacktestEngine:
    def __init__(self, initial_capital: float = 100000):
        self.initial_capital = initial_capital

    def run(self, df: pd.DataFrame):
        df = df.copy()

        position = 0  # 0 = 空手, 1 = 持有
        entry_price = 0

        equity = self.initial_capital
        equity_curve = []

        for i in range(len(df)):
            row = df.iloc[i]
            price = row["Close"]
            signal = row["signal"]

            # ===== 買進 =====
            if position == 0 and signal == 1:
                position = 1
                entry_price = price

            # ===== 賣出 =====
            elif position == 1 and signal == -1:
                pnl = (price - entry_price) / entry_price
                equity *= (1 + pnl)

                position = 0
                entry_price = 0

            equity_curve.append(equity)

        df["equity"] = equity_curve

        return df