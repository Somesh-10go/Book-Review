from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database
import json
import logging

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/books", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(database.get_db)):
    """
    Fetch all books, trying cache first. On cache miss, read from DB and update cache.
    """
    try:
        if database.redis_client:
            cached = database.redis_client.get("books")
            if cached:
                return json.loads(cached)
    except Exception as e:
        logger.warning(f"Redis read failed: {e}")

    books = crud.get_books(db)

    try:
        if database.redis_client:
            serialized_books = json.dumps([book.__dict__ for book in books])
            database.redis_client.set("books", serialized_books)
    except Exception as e:
        logger.warning(f"Redis write failed: {e}")

    return books


@router.post("/books", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    """
    Add a new book to the database. Invalidates cache.
    """
    new_book = crud.create_book(db, book)

    # Invalidate cache
    try:
        if database.redis_client:
            database.redis_client.delete("books")
    except Exception as e:
        logger.warning(f"Redis cache invalidation failed: {e}")

    return new_book
