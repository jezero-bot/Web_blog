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
            return True
        else:
            return False

    def login(self):
        pass
    def get_blogs(self):
        pass


