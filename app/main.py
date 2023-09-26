from typing import Optional, List
from fastapi import  FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, get_db
from .routers import post, user


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency




while True:
    try: 
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', 
                                password = 'Trunghieu1707', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection succesfull")
        break
    except Exception as error:
        print("Connecting database is failed")
        print("Error: " , error)
        time.sleep(2)

my_posts = [{"title" : "title of post 1", "content" : "content of post 1", "id" : 1}, 
            {"title": "favorite food","content": "I like pizza", "id" : 2}
            ]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i   

app.include_router(post.router)
app.include_router(post.user)

@app.get("/")
async def root():
    return {"message": "Hello World from API"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    
    posts = db.query(models.Post).all()
    return {"data": "success"  }


    