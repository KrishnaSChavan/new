from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean,func,DateTime, TIMESTAMP, text
from sqlalchemy.orm import relationship

# class Post(Base):
#     __tablename__ = 'post_alch'
#     __allow_unmapped__ = True

#     id = Column(Integer, primary_key=True,nullable=False)
#     title = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     published = Column(Boolean, server_default='TRUE',nullable=False)
#     time = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
#     owner_id = Column(Integer,ForeignKey("users.id",ondelete="Cascade"),nullable=False)
#     comment = Column(String,nullable=False)

#     owner = relationship("User")
    

class User(Base):
    __tablename__ = 'users'
    __allow_unmapped__ = True
    name = Column(String, nullable=True)
    id = Column(Integer, primary_key=True,nullable=False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP (timezone=True),nullable=False, server_default=text ('now() '))
    
    

# class Vote(Base):
    
#     __tablename__ = 'votes'
#     __allow_unmapped__ = True
#     user_id = Column(Integer,ForeignKey("users.id",ondelete="Cascade"),primary_key=True,nullable=False)
#     post_id = Column(Integer, ForeignKey("post_alch.id",ondelete="Cascade"),primary_key=True,nullable=False)

# class tab(Base):
#     __tablename__ = 'post'
    
#     id=Column(Integer,primary_key=True,nullable=False)
#     title= Column(String,nullable=False)
#     content= Column(String,nullable=False)
#     published=Column(Boolean,nullable=False,server_default='TRUE')