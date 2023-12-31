import time
import psycopg2
from sqlalchemy import create_engine
from psycopg2.extras import RealDictCursor
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


while True:
    try: 
        conn = psycopg2.connect(host = f'{settings.database_hostname}', database = f'{settings.database_name}', user = f'{settings.database_username}', 
                                password = f'{settings.database_password}', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        # print("Database connection succesfull")
        break
    except Exception as error:
        print("Connecting database is failed")
        print("Error: " , error)
        time.sleep(2)