from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

#take email and password
class usercreate(BaseModel):
    email : EmailStr
    password : str
    class Config:
        orm_mode = True


# get email and id
class userout(BaseModel):
    id: int
    email : EmailStr
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title :str
    content :str 
    published : bool = True


class PostCreate(PostBase):
    pass
    

class PostResponse(PostBase):
    id : int
    owner_id : int
    time : datetime
    owner : userout
    
    # convert to python dictionary
    class Config:
        orm_mode = True



# Get user password
class userpass(BaseModel):
    password : str
    class Config:
        orm_mode = True

# user login
class userlogin(BaseModel):
    email : EmailStr
    password : str
    class Config:
        orm_mode = True

class token(BaseModel):
    access_token : str
    token_type : str

class token_data(BaseModel):
    id : str



class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)