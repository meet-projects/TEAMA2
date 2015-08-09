from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#PLACE YOUR TABLE SETUP INFORMATION HERE

class User(Base):
	_tablename_= 'user'
	id = Column(Integer,primary_key=True)
	name = Column(String(60))
	username = Column(String(60))
	password = Column(String(60))
	email = Column(String(60))
	birthday = Column(Integer)
	birthmonth = Column(String(30))
	birthyear = Column(Integer)

class Post(Base):
        _tablename_='post'
        id = Column(Integer,primary_key=True)
        group_id = Column(Integer, ForeignKey('group.id'))
        group= relationship(Group)
        user_poster_id = Column(Integer, ForeignKey('user.id'))
        user = relationship(User)
        content = Column(String(100))
        

class Group(Base):
        _tablename_= 'group'
        id = Column(Integer,primary_key=True)
        name = Column(String(50))
        picture = Column(String)
