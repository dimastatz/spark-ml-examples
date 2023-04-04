import cruncher
from tests.common import spark
from tests.fixtures.tenant_fixture import *


def test_basic():
    df = cruncher.crunch(spark=spark)
    assert df == None


def test_crunch(tenant):
    assert tenant == 1