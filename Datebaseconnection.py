import sqlite3
from sqlite3 import Error


# Creates the database
def userDatabaseTest(connection):
    connect = None
    try:
        connect = sqlite3.connect(connection)
        print('connection to database was successful'.upper())
    except Error as oops:
        print('An error occurred while trying to connect:', oops)
    return connect


# Executes the table queries
# Takes the query as a parameter
def create_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"The query has been executed successfully")
    except Error as oops:
        print(f"There has been an error: {oops}")


# Executes the insert into queries
# Takes the query as a parameter
def read_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as oops:
        print(f"There has been an error: {oops}")


# This variable holds the Person table
person_table = """
CREATE TABLE IF NOT EXISTS 
  userInfo (
  pinNumber      INTEGER  PRIMARY KEY,
  firstName      TEXT     NOT NULL,
  lastName       TEXT     NOT NULL,
  gender         TEXT,
  weight         TEXT,
  height         TEXT,
  bmi            TEXT,
  email          TEXT     NOT NULL,
  secretQuestion INTEGER  NOT NULL,
  answer         TEXT     NOT NULL,
  goal           TEXT,
  previousDay    TEXT
);
"""

connecting = userDatabaseTest("userDatabaseTest")
create_table(connecting, person_table)  # Adds the person table to the database
