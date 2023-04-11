from script1 import load_list_to_df
from tests.utils.tenant_fixture import *


def test_always_passes():
    assert True


def test_load_list_to_df(spark_session):
    df = load_list_to_df(spark_session)
    assert df.count() == 3