import mysql.connector
from app.config import DATABASE_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)