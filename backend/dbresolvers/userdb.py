from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class OneUser(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    nickname = Column(String)
    email = Column(String)
    password = Column(String)


class UserDataResolver(object):
    def __init__(self):
        sqlalchemy_database_uri = 'mysql+pymysql://users_db_solver:related_pass@localhost/playground'
        self.engine = create_engine(sqlalchemy_database_uri)
        self.session = Session(bind=self.engine)

    def __del__(self):
        self.session.close()

    def get_all_users(self):
        return self.session.query(OneUser.user_id, OneUser.email, OneUser.nickname, OneUser.password).all()

    def add_user_to_db(self, nick, eml, passwd):
        user_to_add = OneUser(nickname=nick, email=eml, password=passwd)
        self.session.add(user_to_add)

    def delete_user_from_db(self, uid):
        user_to_delete = self.session.query().filter(OneUser.user_id == uid).one()
        self.session.delete(user_to_delete)

    # TODO: consider there is no double accounts and change .all() to .one()
    def get_user_from_db(self, nick):
        return self.session.query(OneUser).filter(OneUser.nickname == nick).all()

    def check_user_validity(self, nickname_str, email_str):
        dnick_user_list = self.session.query(OneUser).filter(OneUser.nickname == nickname_str).all()
        demail_user_list = self.session.query(OneUser).filter(OneUser.email == email_str).all()
        if dnick_user_list or demail_user_list:
            return False
        return True

    def authentificate(self, nickname_str, password):
        dnick_user = self.session.query(OneUser).filter(OneUser.nickname == nickname_str)
        return self.session.query(dnick_user.exists().scalar())

    def commit_session(self):
        self.session.commit()



