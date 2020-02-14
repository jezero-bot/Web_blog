import uuid
from src.common.database import Database


class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": self.email})
        if data is not None:
            return cls(**data)
    @classmethod
    def get_by_id(cls, _id):
         data = Database.find_one("users", {"_id": _id})
         if data is not None:
             return cls(**data)

    @staticmethod
    def valid_login(self, email, password):
        user = user.get_by_email(email)
        if user is not None:
            return user.password == password
        return False

    @sclassmethod
    def register(cls, email, password):
        user = user.get_by_email(email)
        if user is None:
            new_user = User(email,password)
            new_user.saveToMongo()
            session["email"] = email
            return True
        else:
            return False
    @staticmethod
    def login(self):
        session("email") = user_email

    @staticmethod
    def logout(self):
        session("email") = None

    def get_blogs(self):
        pass

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }
    def saveToMongo(self):
        Database.insert("users", self.json())
