from fastapi import FastAPI
from . import models,config
from app.database import engine
from app.routers import post,user,sqla,auth,vote

from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind=engine)



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(post.router)
app.include_router(user.router)
# app.include_router(sqla.router)
# app.include_router(auth.router)
# app.include_router(vote.router)

@app.get("/")
def login():
    return {"Hello": "I am usind docker"}









