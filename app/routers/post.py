from app.run import conn,cursor
from .. import models
from fastapi import Response,status,HTTPException,Depends,APIRouter
from app.schemas import PostCreate,PostResponse
from app.database import engine,get_db
from sqlalchemy.orm import Session
from typing import Optional,List

router = APIRouter(
    prefix= '/posts',
    tags=['post']
)







@router.get("/")
def get_post():
    try:
        cursor.execute("""SELECT * FROM post """)
        post = cursor.fetchall()
        
    except Exception as e:
        print("Exception",e)

    return post


@router.post("/",status_code=status.HTTP_201_CREATED)
def create(post : PostCreate,db:Session = Depends(get_db)):
    cursor.execute("""INSERT INTO post (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    
    return new_post

@router.get('/latest')
def get_latest():
    post = 1
    return post

@router.put('/{id}')
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


@router.get("/{id}")
def get_post(id:int, response : Response): 
    cursor.execute(""" SELECT * FROM post WHERE id = %s""",(str(id), ))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    return post



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""DELETE FROM post WHERE id = %s RETURNING *""",(str(id),))

    deleated = cursor.fetchone()
    conn.commit()
    if deleated == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)



