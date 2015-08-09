from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE

class User(Base):
	__tablename__= 'user'
	id = Column(Integer,primary_key=True)
	name = Column(String(60))
	username = Column(String(60))
	password = Column(String(60))
	email = Column(String(60))
	birthday = Column(Integer)
	birthmonth = Column(String(30))
	birthyear = Column(Integer)

class Post(Base):
        __tablename__='post'
        id = Column(Integer,primary_key=True)
        group_id = Column(Integer, ForeignKey('group.id'))
        group= relationship(Group)
        user_poster_id = Column(Integer, ForeignKey('user.id'))
        user = relationship(User)
        content = Column(String(100))
        

class Group(Base):
        __tablename__= 'group'
        id = Column(Integer,primary_key=True)
        name = Column(String(50))
        picture = Column(String)
