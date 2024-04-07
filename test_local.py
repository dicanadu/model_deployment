from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_api_get_root():
    r = client.get("/")
    assert r.status_code == 200
