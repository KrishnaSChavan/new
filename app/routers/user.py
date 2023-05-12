from .. import models
from fastapi import status,HTTPException,Depends,APIRouter
from app.schemas import usercreate,userout,userpass
from app.database import engine,get_db
from sqlalchemy.orm import Session
from .. import utils

router = APIRouter(
    prefix='/user',
    tags=["user"]
)

@router.post('/create',status_code=status.HTTP_201_CREATED,response_model=userout)
def create_user(user:usercreate,db: Session = Depends(get_db)):

    has_password = utils.hash(user.password)
    user.password = has_password
    new_user = models.User(**user.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    
    
        return new_user
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail='User already exists')

@router.get('/password/{id}',response_model=userpass)
def passw(id:int,db: Session = Depends(get_db)):
    use = db.query(models.User).filter(models.User.id == id).first()
    if use is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id:{id} not nound")
    print(use)
    return use

@router.get('/user/{id}',response_model=userout)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id ==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with {id} not found')
    
    return user
