from fastapi.testclient import TestClient


def test_create_vacancy(client: TestClient, use_organization):
    data = {
        'title': 'vacancy',
        'description': 'very long very accurate description of the vacancy',
        'pay': 0,
        'worktime': '',
    }
    organization = client.get('/organizations/').json()[0]
    response = client.post(
        f'/organizations/{organization["slug"]}/vacancies/', json=data)

    assert response.status_code == 200, response.json()


def test_create_invalid_vacancy(client: TestClient, use_organization):
    data = {
        'title': 'vacancy',
        'description': 'short description',
        'pay': 0,
        'worktime': '',
    }
    organization = client.get('/organizations/').json()[0]
    response = client.post(
        f'/organizations/{organization["slug"]}/vacancies/', json=data)

    assert response.status_code == 422, response.json()


def test_vacancies_exist(client: TestClient, use_vacancy):
    response = client.get('/vacancies/')
    assert response.status_code == 200
    assert len(response.json()) > 0
