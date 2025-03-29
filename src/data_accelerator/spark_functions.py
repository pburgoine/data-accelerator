import pyspark.sql.functions as sf
from pyspark.sql import DataFrame


def add_column(df: DataFrame, col_name: str) -> DataFrame:
    """Adds a column to a dataframe.

    Args:
        df: The dataframe.
        col_name: The name of the column added.

    Returns:
        The dataframe with a new column added.

    """
    return df.withColumn(col_name, sf.lit(1))
