from fastapi.testclient import TestClient
from routes import app

client = TestClient(app)

def test_get_version():
    response = client.get('/version')
    assert response.status_code == 200
    assert response.json() == {"version": "v0.0.1"}

def test_get_temperature():
    response = client.get('/temperature')
    assert response.status_code == 200