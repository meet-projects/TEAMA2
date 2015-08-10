from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Group, User, Post, GroupUser

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



group = Group(name = 'a')
session.add(group)
session.commit()

group1 = Group(name = 'b')
session.add(group1)
session.commit()

group2 = Group(name = 'c')
session.add(group2)
session.commit()
