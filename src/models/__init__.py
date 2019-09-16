# Copyright 2019 by Mihail Butnaru
# All rights reserved.
""" Postgres Connectivity """
from src.config import Config
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

postgres_engine = create_engine(Config().DATABASE_CONNECTION)

# Session class created configured
Session = sessionmaker(bind=postgres_engine)

Base = declarative_base()

@contextmanager
def session_scope():
    """ Provide a transactional scope around a series of operations. """
    session = Session()
    Base.metadata.create_all(postgres_engine) # creates all the tables
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
