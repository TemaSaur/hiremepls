from fastapi.testclient import TestClient


def test_upload_resume_unauthorized(client: TestClient):
    with open('main.py', 'rb') as file:
        response = client.post(
            '/resumes/', files={'file': ('main.py', file, 'image/jpeg')})
        assert response.status_code == 401
