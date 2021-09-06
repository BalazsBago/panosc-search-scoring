# testing suite for Panosc Search Scoring
# 

from fastapi.testclient import TestClient
from app import app

client = TestClient(app.app)

def test_main():
  response = client.get("/")
  
  assert response.status_code == 200

  payload = response.json()
  payload_keys = list(payload.keys())
  for key in ["application", "description", "version","started-time","current-time","uptime"]:
    assert key in payload_keys

def test_app_config():
  config = client.app.state.config

  assert 'Config' in str(type(config))
  assert config.database == 'pss_test'
  assert config.mongodb_url == "mongodb://127.0.0.1:27017"

