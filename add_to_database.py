from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Group, User, Post

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

group=Group(name="hugafriend")
session.add(group)
session.commit()

user=User(name="Hen",username="HenG",password="HenG",email="hennygrr28@gmail.com")
session.add(user)
session.commit()
