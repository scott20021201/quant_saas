import pandas as pd


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """
    Calculate RSI indicator

    series : price series (usually Close)
    period : RSI period (default 14)
    """

    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi