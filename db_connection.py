import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
connection_string = os.getenv('DB_URL')


def connect_db():
    try:
        conn = psycopg2.connect(connection_string)
        return conn
    except Exception as e:
        print(f"Error connecting DB:{str(e)}")

