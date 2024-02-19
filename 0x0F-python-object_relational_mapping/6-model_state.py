"""
a python file that contains the class definition of a State and an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with maximum 128 characters and can’t be null
"""
# Import SQLAlchemy and other required modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
# Create an engine that connects to the MySQL database
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3], pool_preping=True)

# create a base class that contains the metadata and a constructor
Base = declarative_base()

# Define a class that representsthe State table
class State(Base):
    # specify the table name and engine
    __tablename__ = 'states'
    __table_args__ = {'mysql_engine':'InnoDB'}

    # Define the columns and their types
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    # Define a constructor that accepts the column values as arguements
    def __init__(self, name):
        self.name = name
# Create the table in the database
Base.metadata.create_all(engine)
# Create a session object that allows you to interact with the databse
Session = sessionmaker(bind=engine)
session = Session()
