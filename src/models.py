import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, ForeignKey('Follower.user_from_id'), primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))



class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    type = Column(String(250))
    url= Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('person.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250))
    autor_id = Column(String(250),ForeignKey('User.UserId'))
    post_id = Column(String(250),ForeignKey('Post.id'))
    
    

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, ForeignKey('Media.id'), primary_key=True)
    user_id = Column(String(250), ForeignKey('User.id'))
    

class Follower(Base):
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, primary_key=True)
    user_id = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base

render_er(Base, 'diagram.png')