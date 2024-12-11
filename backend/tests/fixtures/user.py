import pytest


user_data = {
    'email': 'default@email.com',
    'password': 'password',
    'full_name': 'Default User',
    'course': 1,
}
login_data = {
    'email': user_data['email'],
    'password': user_data['password']
}


@pytest.fixture(scope="function")
def use_user(client):
    client.post('/auth/register', json=user_data)


@pytest.fixture(scope="function")
def use_loggedin(client, use_user):
    client.cookies = client.post('/auth/login', json=login_data).cookies
