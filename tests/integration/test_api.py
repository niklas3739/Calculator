import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_add_endpoint(client):
    res = client.get("/api/add", params={"a": 2, "b": 3})
    assert res.status_code == 200
    
    body = res.json()
    assert body["operation"] == "add"
    assert body["result"] == 5

def test_divide_endpoint_ok(client):
    res = client.get("/api/divide", params={"a": 10, "b": 4})
    assert res.status_code == 200
    assert res.json()["result"] == 2.5

def test_divide_endpoint_zero(client):
    res = client.get("/api/divide", params={"a": 10, "b": 0})
    assert res.status_code == 400
    assert res.json()["detail"] == "Cannot divide by zero."

def test_modulo_endpoint_ok(client):
    res = client.get("/api/modulo", params={"a": 10, "b": 3})
    assert res.status_code == 200
    assert res.json()["result"] == 1

def test_modulo_endpoint_zero(client):
    res = client.get("/api/modulo", params={"a": 10, "b": 0})
    assert res.status_code == 400
    assert res.json()["detail"] == "Cannot modulo by zero."
