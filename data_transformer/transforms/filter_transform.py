from .base_transform import BaseTransform
import pandas as pd


class FilterTransform(BaseTransform):
    def __init__(self, condition):
        """
        Filter DataFrame based on a condition

        Args:
            condition (str): Pandas-compatible filtering condition
        """
        self.condition = condition

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.query(self.condition)


# transforms/aggregation_transform.py
from .base_transform import BaseTransform
import pandas as pd


class AggregationTransform(BaseTransform):
    def __init__(self, group_by, agg_dict):
        """
        Perform aggregation on DataFrame

        Args:
            group_by (list): Columns to group by
            agg_dict (dict): Aggregation specifications
        """
        self.group_by = group_by
        self.agg_dict = agg_dict

    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.groupby(self.group_by).agg(self.agg_dict)