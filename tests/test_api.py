from fastapi.testclient import TestClient
from app import app
client=TestClient(app)

def test_health():
    assert client.get("/health").status_code==200

def test_model_endpoint():
    r=client.get("/model")
    assert r.status_code==200
    assert "registry" in r.json()

def test_prediction_endpoint():
    r=client.post("/predict",json={"cpu":80,"memory":80,"latency_ms":120,"error_rate":4,"packet_loss":2,"disk_io":180})
    assert r.status_code==200
