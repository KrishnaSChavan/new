from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from app.database import get_db
from .. import models
from app.schemas import userlogin

router = APIRouter(
    tags= ['Authentication']
)


@router.post('/login')
def login(user_credentials:userlogin,db: Session = Depends(get_db)):
    
    user = db.query(models.user).filter(models.user.email == user_credentials.email)