import pyspark.sql.functions as sf
from pyspark.sql import DataFrame


def add_column(df: DataFrame, col_name: str) -> DataFrame:
    return df.withColumn(col_name, sf.lit(1))
