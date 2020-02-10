
from src.common.Database import Database
import uuid
import datetime

class Post(object):

    def __init__(self,blog_id,title,author,content,created_date=datetime.datetime.utcnow(),_id=None):
        self.blog_id = blog_id
        self.title = title
        self.author = author
        self.content = content
        self._id  = uuid.uuid4().hex if _id is None else _id
        self.created_date = created_date

    def saveToMongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog-id': self.blog_id,
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'created_date': self.created_date

    @classmethod
    def getFromMongo(cls,id):
        post_data = Database.find_one(collection='posts',query={'_id': id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
