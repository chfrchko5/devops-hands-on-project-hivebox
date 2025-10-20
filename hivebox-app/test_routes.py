from fastapi.testclient import TestClient
from routes import app
from version import get_version
from api_data import average_temps

client = TestClient(app)

def test_get_version():
    response = client.get('/version')
    assert response.status_code == 200
    assert response.json() == {"version": get_version()}

def test_get_temperature():
    response = client.get('/temperature')
    value = response.json()
    temp = value["average temperature"].split()[0]
    assert response.status_code == 200
    assert str(temp) == str(round(average_temps, 2))