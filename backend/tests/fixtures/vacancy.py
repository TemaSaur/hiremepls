import pytest
from fastapi.testclient import TestClient


data = {
    'title': 'vacancy',
    'description': 'very long very accurate description of the vacancy',
    'pay': 0,
    'worktime': '',
}


@pytest.fixture(scope="function")
def use_vacancy(client: TestClient, use_organization):
    organization = client.get('/organizations/').json()[0]
    client.post(
        f'/organizations/{organization["slug"]}/vacancies/', json=data)
