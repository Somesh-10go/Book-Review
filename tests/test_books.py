# tests/test_books.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# -----------------------
# ✅ Book Endpoint Tests
# -----------------------

def test_create_book():
    response = client.post("/books", json={"title": "somesh book", "author": "somesh"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "somesh book"
    assert data["author"] == "somesh"
    assert "id" in data


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# --------------------------
# ✅ Review Endpoint Tests
# --------------------------

def test_create_review():
    # Create a book first
    book_response = client.post("/books", json={"title": "Reviewable Book", "author": "Author X"})
    book_id = book_response.json()["id"]

    # Post a review
    review_payload = {"content": "Awesome!", "rating": 5}
    response = client.post(f"/books/{book_id}/reviews", json=review_payload)
    assert response.status_code == 200
    review_data = response.json()
    assert review_data["content"] == "Awesome!"
    assert review_data["rating"] == 5
    assert review_data["book_id"] == book_id


def test_get_reviews_for_book():
    # Create a book
    book_response = client.post("/books", json={"title": "Book With Reviews", "author": "Author Y"})
    book_id = book_response.json()["id"]

    # Add 2 reviews
    client.post(f"/books/{book_id}/reviews", json={"content": "Nice read", "rating": 4})
    client.post(f"/books/{book_id}/reviews", json={"content": "Loved it", "rating": 5})

    # Fetch reviews
    response = client.get(f"/books/{book_id}/reviews")
    assert response.status_code == 200
    reviews = response.json()
    assert isinstance(reviews, list)
    assert len(reviews) >= 2
    assert all(review["book_id"] == book_id for review in reviews)
