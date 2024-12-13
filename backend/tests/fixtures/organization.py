import pytest
from fastapi.testclient import TestClient


data = {
    'title': 'org',
    'description': 'a long and valid description of the organization'
}


@pytest.fixture(scope="function")
def use_organization(client: TestClient):
    response = client.post('/organizations/', json=data)
