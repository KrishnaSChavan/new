from pydantic import BaseModel,EmailStr
from datetime import datetime




class PostBase(BaseModel):
    title :str
    content :str 
    published : bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id : int
    
    

    class Config:
        orm_mode = True

class usercreate(BaseModel):
    email : EmailStr
    password : str


class userd(BaseModel):
    email : str
    time : datetime
    id : int