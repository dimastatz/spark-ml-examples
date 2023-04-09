from script1 import load_list_to_df
from tests.utils.common import spark


def test_always_passes():
    assert True


def test_load_list_to_df():
    df = load_list_to_df(spark)
    assert df.count() == 3