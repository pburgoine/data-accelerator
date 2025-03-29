from pyspark.sql import SparkSession

import pytest


def pytest_addoption(parser):
    parser.addoption("--connect", action="store_true", default=None)


@pytest.fixture(scope="session")
def use_connect(pytestconfig):
    return pytestconfig.getoption("connect")


@pytest.fixture
def spark(use_connect) -> SparkSession:
    if use_connect:
        spark_session = (
            SparkSession.builder.remote("sc://localhost:15002")  # type: ignore
            .appName("Spark Connect Pytest Fixture")
            .getOrCreate()
        )
    else:
        spark_session = (
            SparkSession.builder.master("local")  # type: ignore
            .appName("Spark Connect Pytest Fixture")
            .getOrCreate()
        )
    return spark_session
