import pytest
from app.models.user_model import User

@pytest.fixture
def new_user():
    return {"username": "testuser", "password": "testpassword"}

def test_register_user(test_client, new_user):
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 201
    assert response.json["message"] == "Usuario creado exitosamente"
    
def test_register_duplicate_user(test_client, new_user):
    response = test_client.post("/api/register", json=new_user)
    assert response.status_code == 400
    assert response.json["error"] == "El nombre de usuario ya esta en uso"
    
def test_login_user(test_client, new_user):
    login_credentials = {
        "username": new_user["username"],
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 200
    assert response.json["access_token"]
    
def test_login_invalid_user(test_client, new_user):
    login_credentials = {
        "username": "nousername",
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credenciales invalidas"
    
def test_login_wrong_password(test_client, new_user):
    login_credentials = {"username": new_user["username"], "password": "wrongpassword"}
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credenciales invalidas"
