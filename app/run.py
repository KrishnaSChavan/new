from typing import Optional
from random import randrange
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()
class Post(BaseModel):
    title :str
    content :str 
    published : bool = True


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


@app.get("/post")

def get_post():
    cursor.execute("""SELECT * FROM post """)
    posts = cursor.fetchall()
    print(posts)
    return {'data': posts}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create(post : Post):
    cursor.execute("""INSERT INTO post (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"message": new_post}

@app.get('/posts/latest')
def get_latest():
    post = my_posts[len(my_posts)-1]
    return {"latest post is": post}

@app.put('/posts/{id}')
def put_post(id:int,post:Post):
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
    
    return {"post": post}
    

@app.get("/posts/{id}")
def get_post(id:int, response : Response):
    cursor.execute(""" SELECT * FROM post WHERE id = %s""",(str(id), ))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    return {"id": post}



@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""DELETE FROM post WHERE id = %s RETURNING *""",(str(id),))

    deleated = cursor.fetchone()
    conn.commit()
    if deleated == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)