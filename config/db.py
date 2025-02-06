from pymysql import OperationalError
from sqlalchemy import create_engine, MetaData

engine= create_engine("mysql+pymysql://root@localhost:3306/test")
meta = MetaData()
conn = engine.connect()

def check_db_connection():

    try:
       
        with engine.connect() as conn:
            conn.connection.ping()  
        print("Database connection successful!")
    except OperationalError as e:
        print("Error connecting to the database:", e)


check_db_connection()