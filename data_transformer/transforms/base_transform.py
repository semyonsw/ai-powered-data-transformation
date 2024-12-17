from abc import ABC, abstractmethod
import pandas as pd


class BaseTransform(ABC):
    """Abstract base class for all data transformations"""

    @abstractmethod
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply transformation to input DataFrame

        Args:
            df (pd.DataFrame): Input DataFrame

        Returns:
            pd.DataFrame: Transformed DataFrame
        """
        pass

    def __repr__(self):
        """Provide a string representation of the transform"""
        return f"{self.__class__.__name__}"