from jose import JWTError, jwt
from datetime import datetime,timedelta
from app import schemas,models,database
from fastapi import status, exceptions,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    enc = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM) #use algorithm
    return enc

def verify_access_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM] ) #use algorithms

        id:str = payload.get("user_id")
        print(id)
        if id is None:
            raise credentials_exception
        td = schemas.token_data(id=id)
        
        return td
    except JWTError as e:
        print(e)
        raise credentials_exception
    
    

def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED,detail=f"Invalid",headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)
    
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return token







#a12ew342rqqdqda3wn@gmail.com