import pytest
from script1 import load_list_to_df


def test_always_passes():
    assert True


def test_load_list_to_df():
    df = load_list_to_df()
    assert df.count() == 3