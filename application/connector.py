from application.database.data_access import DataAccess

class Connector():

    def extract_joke(self):
        da = DataAccess()
        row = da.get_joke()
        return row

    def extract_num_of_jokes(self):
        da = DataAccess()
        num = da.get_num_of_jokes()
        return num
