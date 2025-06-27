from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database
import json

router = APIRouter()

@router.get("/books", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(database.get_db)):
    try:
        cached = database.redis_client.get("books") if database.redis_client else None
        if cached:
            return json.loads(cached)
    except:
        pass  # cache error ignored

    books = crud.get_books(db)
    try:
        if database.redis_client:
            database.redis_client.set("books", json.dumps([book.__dict__ for book in books]))
    except:
        pass

    return books

@router.post("/books", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db, book)
