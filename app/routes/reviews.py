from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

@router.get("/books/{book_id}/reviews", response_model=list[schemas.ReviewOut])
def get_reviews(book_id: int, db: Session = Depends(database.get_db)):
    return crud.get_reviews(db, book_id)

@router.post("/books/{book_id}/reviews", response_model=schemas.ReviewOut)
def post_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(database.get_db)):
    return crud.add_review(db, book_id, review)
