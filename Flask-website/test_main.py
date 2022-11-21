import pytest
from main import app

@pytest.fixture

def client():
    client = app.test_client()
    return client
    
def test_get_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    
def test_logout_returns_302(client):
    response = client.get("/logout")
    assert response.status_code == 302