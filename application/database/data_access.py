from dotenv import load_dotenv
import os
import pymysql

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_DATABASE = os.getenv("DB_DBNAME")

conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    database=DB_DATABASE
)

