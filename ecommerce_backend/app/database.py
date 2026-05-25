import psycopg2
from app.config import settings

def get_connections():
    return psycopg2.connect(settings.DATABASE_URL)

def get_db():
    db = get_connections()
    try:
        yield db
    finally:
        db.close()