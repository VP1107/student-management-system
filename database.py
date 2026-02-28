import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

def connect_database():
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_database = os.getenv("DB_NAME")
    
    if not all([db_host, db_database, db_password, db_user]):
        raise ValueError("One or More Environment Variables are Missing")
    
    mydb = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_database,
    )
    return mydb


def create_table():
    db = connect_database()
    cursor = db.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS students(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        grade VARCHAR(1),
        email VARCHAR(50) UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    cursor.execute(query)

    cursor.close()
    db.close()