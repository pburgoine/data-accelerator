from data_accelerator.spark_functions import add_column


def test_my_functions(spark):
    df = spark.sql("SELECT 1 AS col1").transform(lambda df: add_column(df, "col2"))
    assert df.columns == ["col1", "col2"]
