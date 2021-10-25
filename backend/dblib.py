from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://book-service:pass123@localhost/playground'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = Session(bind=engine)


class OneUser(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    nickname = Column(String)
    email = Column(String)
    password = Column(String)


def add_user_to_db(nick, eml, passwd):
    user_to_add = OneUser(nickname=nick, email=eml, password=passwd)
    session.add(user_to_add)
    session.commit()


def delete_user_from_db(uid):
    user_to_delete = session.query().filter(OneUser.user_id == uid).one()
    session.delete(user_to_delete)
    session.commit()


# Could be made better, but I dont know how
def select_user_from_db(criteria, key):
    users_list = session.query(OneUser).filter(criteria == key).all()
    return users_list
