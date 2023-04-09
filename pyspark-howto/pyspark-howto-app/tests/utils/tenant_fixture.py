import pytest
import mongomock

@pytest.fixture
def tenant():
    return 1


@pytest.fixture(scope="session")
def mongo() -> mongomock.MongoClient:
    client = mongomock.MongoClient()
    yield client
    client.close()


