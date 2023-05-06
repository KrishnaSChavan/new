from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean,func,DateTime, TIMESTAMP, text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'post_alch'


    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE',nullable=False)
    time = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="Cascade"),nullable=False)

    owner = relationship("User",)
    

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,nullable=False)
    email = Column(String, nullable=False,unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP (timezone=True),nullable=False, server_default=text ('now() '))
    
