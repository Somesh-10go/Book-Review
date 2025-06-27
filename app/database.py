from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import redis

# SQLite DB connection string
DATABASE_URL = "sqlite:///./books.db"
REDIS_URL = "redis://localhost:6379"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Redis setup (optional, mockable)
try:
    redis_client = redis.Redis.from_url(REDIS_URL)
    redis_client.ping()
except redis.exceptions.ConnectionError:
    redis_client = None

# Dependency to use in FastAPI routes
def get_db():
    db = SessionLocal()  # No parameters passed — avoids "local_kw" injection
    try:
        yield db
    finally:
        db.close()
