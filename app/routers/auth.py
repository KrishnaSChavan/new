from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from app.database import get_db
from .. import models,utils
from app.schemas import userlogin,token
from .. import auth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags= ["Authentication"]
)


@router.post('/login',response_model=token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db)):
    
    ## OAuth2PasswordRequestForm it returns dictonary of username and password ##
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid email')
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid password')
    
    access_token = auth2.create_access_token(data={"user_id":user.id})
 
    return {"access_token" : access_token,"token_type": "bearer"}