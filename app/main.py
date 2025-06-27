from fastapi import FastAPI
from app.routes import books, reviews
from app.database import Base, engine

# Create all tables
#Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router)
app.include_router(reviews.router)
