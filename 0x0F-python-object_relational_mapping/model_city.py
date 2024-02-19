#!/usr/bin/python3
"""
a python file that contains the class definition
of a City and an
instance Base = declarative_base():
"""
# Import SQLAlchemy and other required modules
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sys import argv


class City(Base):
    """
    A base class that contains the metadata and a constructor
    State class:
    inherits from Base Tips
    links to the MySQL table states
    class attribute:
        (id): that represents a column of an auto-generated,
          unique integer, can’t be null and is a primary key
        (name) that represents a column of a
            string with maximum 128 characters and can’t be null
        state_id: represents a column of an integer,
            can’t be null and is  foreign key to states.id
    """
    # specify the table name and engine
    __tablename__ = 'cities'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    # Define the columns and their types
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
    name = Column(String(128))

    def __init__(self, name):
        """
        Define a constructor that accepts the column values as arguements
        """
        self.name = name


if __name__ == "main":
    # Create an engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3], pool_preping=True))
    # Create the table in the database
    Base.metadata.create_all(engine)
