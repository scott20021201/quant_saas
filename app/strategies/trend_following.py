import pandas as pd

from app.strategies.base_strategy import BaseStrategy
from app.indicators.moving_average import sma


class TrendFollowingStrategy(BaseStrategy):
    """
    簡單趨勢追蹤策略：
    SMA20 / SMA50 黃金交叉買進，死亡交叉賣出
    """

    def __init__(self, short_window: int = 20, long_window: int = 50):
        super().__init__(name="trend_following")
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        df["SMA_short"] = sma(df["Close"], self.short_window)
        df["SMA_long"] = sma(df["Close"], self.long_window)

        df["signal"] = 0

        # 黃金交叉：今天短均線 > 長均線，昨天短均線 <= 長均線
        buy_condition = (
            (df["SMA_short"] > df["SMA_long"]) &
            (df["SMA_short"].shift(1) <= df["SMA_long"].shift(1))
        )

        # 死亡交叉：今天短均線 < 長均線，昨天短均線 >= 長均線
        sell_condition = (
            (df["SMA_short"] < df["SMA_long"]) &
            (df["SMA_short"].shift(1) >= df["SMA_long"].shift(1))
        )

        df.loc[buy_condition, "signal"] = 1
        df.loc[sell_condition, "signal"] = -1

        return df