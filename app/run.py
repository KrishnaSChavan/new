from fastapi import FastAPI
from . import models
from app.database import engine,get_db
from app.utils import hash
from app.routers import post,user,sqla,auth

models.Base.metadata.create_all(bind=engine)


app = FastAPI()





app.include_router(post.router)
app.include_router(user.router)
app.include_router(sqla.router)
app.include_router(auth.router)

@app.get("/")
def login():
    return {"Hello": "World"}









