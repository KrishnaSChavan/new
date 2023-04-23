from typing import Optional,List
from random import randrange
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.responses import HTMLResponse
from app.schemas import PostCreate,PostResponse,usercreate,userd
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from app.database import engine,get_db
from sqlalchemy.orm import Session 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()





while True:
    
    try:
        conn = psycopg2.connect(host = 'localhost',database='fastapi1',user='abc',password='-',cursor_factory=RealDictCursor)#(host, databatse, user, password,RealDictCursor for obtaining colums of table)
        cursor = conn.cursor()
        print ("Connected")
        break
    except Exception as e:
        print ("Failed to connect")
        print(e)
        time.sleep(5)


try:
    
    cursor.execute("""ALTER TABLE IF EXISTS public.post_alch
    ADD COLUMN \"time\" time with time zone DEFAULT NOW() RETURNING * """)
    conn.commit()
except Exception as ex:
        print ("")
    

conn.commit()


my_posts = [{"title": "title of post 1", "content": "content of post 1","id":1},{"title": "title of post 1", "content": "content of post 1","id":3}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index(id):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            return i



@app.get("/")
def login():
    return {"Hello": "World"}



@app.get('/sqlalkk',response_model= List[PostResponse])
def test_p(db: Session = Depends(get_db)):
    x = db.query(models.Post).all()
    print(x)
    return  x

@app.post('/sqlalkk/post',status_code=status.HTTP_201_CREATED,response_model= PostResponse)
def post_s(post:PostCreate,db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post

@app.get('/sqlalkk/{id}',response_model=PostResponse)
def post_g(id:int,db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    return  post
    
@app.delete('/sqlalkk/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/sqlalkk/{id}',response_model=PostResponse)
def delete_post(post:PostCreate,id:int,db: Session = Depends(get_db)):
    post_q = db.query(models.Post).filter(models.Post.id == id)

    pos = post_q.first()
    if pos == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    post_q.update(post.dict())
    db.commit()

    return post_q.first()

@app.get("/post")
def get_post():
    try:
        cursor.execute("""SELECT * FROM post """)
        post = cursor.fetchall()
        
    except Exception as e:
        print("Exception",e)

    return post


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create(post : PostCreate,db:Session = Depends(get_db)):
    cursor.execute("""INSERT INTO post (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    
    return new_post

@app.get('/posts/latest')
def get_latest():
    post = my_posts[len(my_posts)-1]
    return post

@app.put('/posts/{id}')
def put_post(id:int,post:PostCreate):
    cursor.execute("""UPDATE post 
                      SET title = %s ,
                          content = %s ,
                          published = %s 
                          WHERE id = %s
                          RETURNING *
                       """,
                       (post.title,post.content,post.published,str(id))
                    )
    updated = cursor.fetchone()
    conn.commit()

    if updated == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
        #return {"post": post}
    
    return post


@app.get("/posts/{id}")
def get_post(id:int, response : Response): 
    cursor.execute(""" SELECT * FROM post WHERE id = %s""",(str(id), ))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    return post



@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""DELETE FROM post WHERE id = %s RETURNING *""",(str(id),))

    deleated = cursor.fetchone()
    conn.commit()
    if deleated == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.post('/user',status_code=status.HTTP_201_CREATED)
def create_user(user:usercreate,db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
