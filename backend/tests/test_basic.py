from fastapi.testclient import TestClient


def test_work(client: TestClient):
    for endpoint in ['/vacancies/', '/organizations/']:
        response = client.get(endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 0
