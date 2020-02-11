



class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_by_email(self):
        Database.find_one("user", email)

    def get_by_id(self):
        pass

    def valid_login(self):
        pass

    def register(self):
        pass

    def login(self):
        pass
    def get_blogs(self):
        pass


