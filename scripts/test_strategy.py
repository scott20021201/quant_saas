import sys
from pathlib import Path

# 讓 Python 可以找到 app 模組
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.data.data_loader import DataLoader
from app.strategies.trend_following import TrendFollowingStrategy
from app.backtest.engine import BacktestEngine

def main():
    loader = DataLoader()

    df = loader.load(
        "2330.TW",
        "2020-01-01",
        "2024-01-01"
    )

    strategy = TrendFollowingStrategy(short_window=20, long_window=50)
    df = strategy.generate_signals(df)

    print(df[df["signal"] != 0][["Close", "SMA_short", "SMA_long", "signal"]].tail(10))
    print()
    print("Buy signals:", (df["signal"] == 1).sum())
    print("Sell signals:", (df["signal"] == -1).sum())
    engine = BacktestEngine(initial_capital=100000)
    df = engine.run(df)

    print()
    print("Final equity:", df["equity"].iloc[-1])


if __name__ == "__main__":
    main()