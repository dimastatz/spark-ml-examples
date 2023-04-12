import pytest
from tests.utils.tenant_fixture import *


def test_always_passes(monkeypatch):
    monkeypatch.setattr('script1.load_list_to_df', lambda _: 1)
    from script1 import load_list_to_df
    assert load_list_to_df(None) == 1


def test_raising_error(monkeypatch):
    def raise_error(spark):
        raise TypeError('error')
     
    monkeypatch.setattr('script1.load_list_to_df', raise_error)
    from script1 import load_list_to_df
    
    with pytest.raises(TypeError) as e:
        load_list_to_df(None)
        assert str(e.value) == 'error'


def test_load_list_to_df(spark_session):
    from script1 import load_list_to_df
    df = load_list_to_df(spark_session)
    assert df.count() == 3