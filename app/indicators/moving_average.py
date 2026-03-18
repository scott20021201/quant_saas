import pandas as pd


def sma(series: pd.Series, window: int) -> pd.Series:
    """
    Simple Moving Average

    Parameters
    ----------
    series : pd.Series
        Price series (usually Close)
    window : int
        Lookback period

    Returns
    -------
    pd.Series
        SMA values
    """
    return series.rolling(window=window).mean()


def ema(series: pd.Series, window: int) -> pd.Series:
    """
    Exponential Moving Average

    Parameters
    ----------
    series : pd.Series
        Price series
    window : int
        Lookback period

    Returns
    -------
    pd.Series
        EMA values
    """
    return series.ewm(span=window, adjust=False).mean()