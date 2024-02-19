#!/usr/bin/python3

"""
a script that prints the State object with
the name passed as argument from the database
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
    states = session.query(State)\
        .filter(State.name == argv[4])\
        .order_by(State.id).all()
    if not states:
        print("Not found", end="\n")
    else:
        for state in states:
            if state is None or state == "":
                print("Not found", end="\n")
            else:
                print("{}".format(state.id))


if __name__ == "__main__":
    main()
