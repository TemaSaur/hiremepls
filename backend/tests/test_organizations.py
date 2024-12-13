from fastapi.testclient import TestClient


def test_create_organization(client: TestClient):
    data = {
        'title': 'org',
        'description': 'a long and valid description of the organization'
    }

    response = client.post('/organizations/', json=data)
    assert response.status_code == 200, response.json()
    assert response.json().get('slug')


def test_organizations_exist(client: TestClient, use_organization):
    response = client.get('/organizations/')
    assert response.status_code == 200, response.json()
    assert len(response.json()) > 0, response.json()
