from fastapi import FastAPI
from . import conn,cursor
from . import models
from app.database import engine,get_db
from app.utils import hash
from app.routers import post,user,sqla,auth

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


try:
    
    cursor.execute("""ALTER TABLE IF EXISTS public.post_alch
    ADD COLUMN \"time\" time with time zone DEFAULT NOW() RETURNING * """)
    conn.commit()
except Exception as ex:
        print ("")
    
conn.commit()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(sqla.router)
app.include_router(auth.router)

@app.get("/")
def login():
    return {"Hello": "World"}




