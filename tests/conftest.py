from pyspark.sql import SparkSession

import pytest


def pytest_addoption(parser):
    parser.addoption("--connect", action="store_true", default=None)


@pytest.fixture(scope="session")
def use_connect(pytestconfig):
    return pytestconfig.getoption("connect")


@pytest.fixture
def spark(use_connect) -> SparkSession:
    spark_session = SparkSession.builder
    if use_connect:
        spark_session = spark_session.remote("sc://localhost:15002")
    return spark_session.appName("Pytest spark fixture").getOrCreate()
