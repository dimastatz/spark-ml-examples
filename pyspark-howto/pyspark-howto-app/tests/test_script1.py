from tests.utils.tenant_fixture import *


def test_always_passes(monkeypatch):
    monkeypatch.setattr('script1.load_list_to_df', lambda x: 1)
    from script1 import load_list_to_df
    assert load_list_to_df(None) == 1


def test_load_list_to_df(spark_session):
    from script1 import load_list_to_df
    df = load_list_to_df(spark_session)
    assert df.count() == 3