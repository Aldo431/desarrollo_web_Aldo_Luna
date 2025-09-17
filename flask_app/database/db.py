from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey # type: ignore
from sqlalchemy.orm import declarative_base, relationship, sessionmaker # type: ignore
import pymysql # type: ignore
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002" 
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URI, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

with open('database/querys.json', 'r', encoding='utf-8') as querys:
    QUERY_DICT = json.load(querys)


# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# -- querys --

def get_last_5_avisos():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["get_last_avisos"], ())
    avisos = cursor.fetchall()
    return avisos