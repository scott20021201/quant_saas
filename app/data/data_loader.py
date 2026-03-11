import pandas as pd
import yfinance as yf
from pathlib import Path


class DataLoader:

    def __init__(self, cache_dir="data/cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def load(self, symbol, start, end):

        cache_file = self.cache_dir / f"{symbol}_{start}_{end}.csv"

        # 如果有 cache 就直接讀
        if cache_file.exists():
            df = pd.read_csv(cache_file, parse_dates=["Date"], index_col="Date")
            return df

        # 下載資料
        df = yf.download(
            symbol,
            start=start,
            end=end,
            progress=False
        )

        if df.empty:
            raise ValueError("No data downloaded")

        df = df.sort_index()

        # 存 cache
        df.to_csv(cache_file)

        return df