import bcrypt

from application.database.data_access import DataAccess
from werkzeug.security import generate_password_hash, check_password_hash

class Connector():

    def extract_joke(self):
        da = DataAccess()
        row = da.get_joke()
        return row

    def extract_num_of_jokes(self):
        da = DataAccess()
        num = da.get_num_of_jokes()
        return num

    def hash_password(self, password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed

    def add_user(self, email, password):
        da = DataAccess()
        print("Printing connector: ")
        print(email, password)
        da.create_user(email, self.hash_password(password))

    def get_user_by_email(self, email):
        da = DataAccess()
        row = da.get_user_by_email(email)
        return row

    def verify_user_by_password(self, email, password):
        da = DataAccess()
        return da.verify_user(email, password)



