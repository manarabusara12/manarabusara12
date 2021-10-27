from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key = True)
  username = Column(String)
  password = Column(Integer)
class Post(Base):
  __tablename__ = 'post'
  id = Column(Integer, primary_key = True)
  username = Column(String)
  Level = Column(String)
  namethebook = Column(String)
  
