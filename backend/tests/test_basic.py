from fastapi.testclient import TestClient


def test_work(client):
    response = client.get('/vacancies/')
    assert response.status_code == 200
