#!/usr/bin/python3

"""
a script that changes the name of a State object from the database
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    """
    Program Entrance
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3], pool_preping=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query the table and print result
    session.commit()
    state = session.query(State)\
                   .filter(State.id == 2)
    record = state.one()
    record.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    main()
