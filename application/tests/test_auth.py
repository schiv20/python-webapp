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
    response = client.post("/login", json={"email": "abdulbari.ibrahim@sky.uk", "password": "123"})
    assert response.status_code == 200
    data = response.get_json()
    assert "token" in data

def test_login_invalid(client):
    response = client.post("/login", json={"email": "user@user", "password": "124"})
    assert response.status_code == 401
