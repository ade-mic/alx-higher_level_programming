#!/usr/bin/python3

"""
a script that lists all State objects from the database hbtn_0e_6_usa
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
    state = session.query(State).first()
    if state is None:
        print("Nothing\n")
    else:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    main()
