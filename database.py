
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def create_post(username,Level,namethebook):
  post = Post(username=username, Level=Level, namethebook=namethebook)
  session.add(post)
  session.commit()
def query_all():
  posts= session.query(Post).all()
  return post

def post_by_Level(Level):
  new_post = session.query(Post).filter_by(Level=Level).all()
  return new_post