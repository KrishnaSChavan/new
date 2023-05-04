from app.run import conn,cursor
from .. import models,auth2
from fastapi import Response,status,HTTPException,Depends,APIRouter
from app.schemas import PostCreate,PostResponse
from app.database import engine,get_db
from sqlalchemy.orm import Session
from typing import Optional,List

router = APIRouter(
    prefix='/sqlalkk',
    tags=["sqlalkk"]
)




@router.get('/',response_model= List[PostResponse]) #List is used to get list of elements in db in form of json
def test_p(db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):
    x = db.query(models.Post).all()
    print(x)
    return  x

@router.post('/post',status_code=status.HTTP_201_CREATED,response_model= PostResponse)
def post_s(post:PostCreate,db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    print(current_user)
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post

@router.get('/{id}',response_model=PostResponse)
def post_g(id:int,db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    return  post
    
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}',response_model=PostResponse)
def update_post(post:PostCreate,id:int,db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):
    post_q = db.query(models.Post).filter(models.Post.id == id)

    pos = post_q.first()
    if pos == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id {id} not found')
    post_q.update(post.dict())
    db.commit()

    return post_q.first()