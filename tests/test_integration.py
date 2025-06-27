# tests/test_integration.py
from fastapi.testclient import TestClient
from app.main import app
from app.database import redis_client

client = TestClient(app)

def test_books_cache_miss_then_hit():
    # Clear Redis cache manually
    if redis_client:
        redis_client.delete("books")

    # First call - cache miss (will populate from DB)
    response_1 = client.get("/books")
    assert response_1.status_code == 200
    assert isinstance(response_1.json(), list)

    # Second call - should hit the cache (same result)
    response_2 = client.get("/books")
    assert response_2.status_code == 200
    assert response_1.json() == response_2.json()
