from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean

class Post(Base):
    __tablename__ = 'post_alch'


    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE',nullable=False)
    
