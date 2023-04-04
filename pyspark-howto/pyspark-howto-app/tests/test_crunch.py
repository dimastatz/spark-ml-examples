import cruncher
from tests.common import spark


def test_basic():
    df = cruncher.crunch(spark=spark)
    assert df == None
