from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, User,Group,Post,GroupUser

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

### These are the commands you just saw live.


# This deletes everything in your database.
session.query(User).delete()
session.query(Group).delete()
session.query(Post).delete()
session.query(GroupUser).delete()
session.commit()

# This adds some rows to the database. Make sure you `commit` after `add`ing!

