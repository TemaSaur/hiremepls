from fastapi.testclient import TestClient


bad_inputs = [
    {
        'email': 'invalid@email',
        'password': 'longpass',
        'full_name': 'Full Name',
        'course': 1,
    },
    {
        'email': 'valid@email.com',
        'password': 'short',
        'full_name': 'Full Name',
        'course': 1,
    },
    {
        'email': 'valid@email.com',
        'password': 'longpass',
        'full_name': 'short',
        'course': 1,
    },
    {
        'email': 'valid@email.com',
        'password': 'longpass',
        'full_name': 'Full Name',
        'course': -1,
    },
]

default_login = {
    'email': 'default@email.com',
    'password': 'password'
}


def test_register(client: TestClient):
    data = {
        'email': 'valid@email.ru',
        'password': 'longpass',
        'full_name': 'Full Name',
        'course': 1,
    }
    response = client.post('/auth/register', json=data)
    assert response.status_code == 200
    res = response.json()
    assert res['email'] == data['email']
    assert res['full_name'] == data['full_name']
    assert res['course'] == data['course']


def test_register_invalid_input(client: TestClient):
    for data in bad_inputs:
        response = client.post('/auth/register', json=data)
        assert response.status_code == 422
        assert len(response.json()['detail']) == 1, response.json()


def test_login(client: TestClient, use_user):
    response = client.post('/auth/login', json=default_login)
    assert response.status_code == 200, response.json()
    assert response.json()['full_name'] == 'Default User'
    assert len(response.cookies) > 0
    assert response.cookies.get('token') != ''


def test_get_me(client: TestClient, use_user):
    client.cookies = client.post('/auth/login', json=default_login).cookies
    response = client.get('/auth/me')
    assert response.status_code == 200


def test_get_me_ready(client: TestClient, use_loggedin):
    response = client.get('/auth/me')
    assert response.status_code == 200


def test_non_unique_user(client: TestClient):
    data = {
        'email': 'valid@email.ru',
        'password': 'longpass',
        'full_name': 'Full Name',
        'course': 1,
    }
    client.post('/auth/register')
    response = client.post('/auth/register')
    assert response.status_code >= 400
