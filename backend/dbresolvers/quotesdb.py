from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OneQuote(Base):
    __tablename__ = 'quotes'
    quote_id = Column(Integer, primary_key=True)
    author = Column(String)
    the_quote = Column(String)


class QuoteDataResolver(object):
    def __init__(self):
        sqlalchemy_database_uri = 'mysql+pymysql://quotes_db_solver:related_pass@localhost/playground'
        self.engine = create_engine(sqlalchemy_database_uri)
        self.session = Session(bind=self.engine)

    def __del__(self):
        self.session.close()

    def add_quote(self, auth, quote):
        quote_to_add = OneQuote(author=auth, the_quote=quote)
        self.session.add(quote_to_add)

    def get_all_quotes(self):
        return self.session.query(OneQuote.quote_id, OneQuote.author, OneQuote.the_quote).all()

    def commit_session(self):
        self.session.commit()
