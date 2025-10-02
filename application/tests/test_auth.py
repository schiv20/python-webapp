import jwt
import datetime
import pytest

SECRET = "testsecret"  # match app config

@pytest.fixture
def client():
    from app import app
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = SECRET
    with app.test_client() as client:
        yield client

def get_token():
    # Helper to generate a valid token
    payload = {
        "sub": "testuser",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def test_login_returns_token(client):
    response = client.post("/login", json={"username": "admin", "password": "password"})
    assert response.status_code == 200
    data = response.get_json()
    assert "token" in data

def test_protected_endpoint_requires_token(client):
    response = client.get("/users")
    assert response.status_code == 401

def test_protected_endpoint_with_token(client):
    token = get_token()
    response = client.get("/users", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code in [200, 204]  # may be empty if no users
