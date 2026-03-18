from abc import ABC, abstractmethod
import pandas as pd


class BaseStrategy(ABC):
    """
    所有策略的基底類別
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        接收市場資料，回傳帶有 signal 欄位的 DataFrame
        """
        pass