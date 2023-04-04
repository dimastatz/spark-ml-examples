from tests.common import spark
from script1 import load_list_to_df
from pyspark.sql import SparkSession


def test_always_passes():
    assert True


def test_load_list_to_df():
    df = load_list_to_df(spark)
    assert df.count() == 3