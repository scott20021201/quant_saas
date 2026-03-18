import sys
from pathlib import Path

# 讓 Python 可以找到 app 模組
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.data.data_loader import DataLoader
from app.indicators.moving_average import sma, ema
from app.indicators.rsi import rsi
from app.indicators.atr import atr

def main():

    loader = DataLoader()

    df = loader.load(
        "2330.TW",
        "2020-01-01",
        "2024-01-01"
    )

    close = df["Close"]

    df["SMA20"] = sma(close, 20)
    df["EMA20"] = ema(close, 20)
    df["RSI14"] = rsi(close, 14)
    df["ATR14"] = atr(df["High"], df["Low"], df["Close"], 14)
    
    print(df[["Close", "SMA20", "EMA20", "RSI14", "ATR14"]].tail())


if __name__ == "__main__":
    main()