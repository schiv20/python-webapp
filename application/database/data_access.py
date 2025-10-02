import bcrypt
from dotenv import load_dotenv
import os
import pymysql
import random

class DataAccess:

    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_DATABASE = os.getenv("DB_NAME")

    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        database=DB_DATABASE
    )

    def get_num_of_jokes(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM joke")
            return cursor.fetchone()[0]

    def get_joke(self) :
        # pick by OFFSET, not by ID (avoids gaps)
        total = self.get_num_of_jokes()
        if total == 0:
            return None
        random_joke = random.randint(0, total - 1)
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT the_joke, punchline FROM joke WHERE ID = %s", (random_joke,))
            return cursor.fetchone()

    def create_user(self, email, password):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO user (Email, Password) VALUES (%s, %s)",
                (email, password)
            )
            self.conn.commit()

    def get_user_by_email(self, email):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM user WHERE Email = %s", (email,))
            return cursor.fetchone()

    def verify_user(self, email, password):
        print("Verifying user in data access")
        print(email, password)
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT Password FROM user WHERE Email = %s", (email,))
                user = cursor.fetchone()
                print(user)
                if not user:
                    return False

                stored_hash = user[0]
                print(stored_hash)
                # bcrypt expects bytes
                return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
        finally:
            self.conn.close()

