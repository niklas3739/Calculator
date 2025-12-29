from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_add_endpoint():
    res = client.get("/api/add", params={"a": 2, "b": 3})
    assert res.status_code == 200
    body = res.json()
    assert body["operation"] == "add"
    assert body["result"] == 5

def test_divide_endpoint_ok():
    res = client.get("/api/divide", params={"a": 10, "b": 4})
    assert res.status_code == 200
    assert res.json()["result"] == 2.5

def test_divide_endpoint_zero():
    res = client.get("/api/divide", params={"a": 10, "b": 0})
    assert res.status_code == 400
    assert res.json()["detail"] == "Cannot divide by zero."
