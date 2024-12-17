from .base_transform import BaseTransform
import pandas as pd


class ColumnSelector(BaseTransform):
    def __init__(self, columns):
        """
        Select specific columns from DataFrame

        Args:
            columns (list): List of column names to select
        """
        self.columns = columns

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[self.columns]