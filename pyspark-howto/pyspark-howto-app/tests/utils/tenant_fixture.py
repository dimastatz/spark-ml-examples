import pytest
import mongomock
from pyspark.sql import SparkSession

@pytest.fixture
def tenant():
    return 1


@pytest.fixture(scope="session")
def mongo_client() -> mongomock.MongoClient:
    client = mongomock.MongoClient()
    yield client
    client.close()


@pytest.fixture
def spark_session():
    session = SparkSession.builder \
        .appName("pyspark-howto-app-1") \
        .config("spark.driver.bindAddress","127.0.0.1") \
        .getOrCreate()
    yield session
    session.stop()




