import uuid
import datetime
from src.common.Database import Database
from src.models.post import Post

class Blog(object):
    def __init__(self,author,title,description,_id=None):
        self.author = author
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if id is None else id

    def newPost(self):
        title = input('enter new title: ')
        content = input('enter new content  : ')
        date = input('enter date or leave blank (in DDMMYYYY format): ')
        if date == '':
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self._id,
                    title=title,
                    author=self.author,
                    content=content,
                    created_date=date)
        post.saveToMongo()


    def getPosts(self):
        return Post.from_blog(self._id)


    def saveToMongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self._id
        }

    @classmethod
    def getFromMongo(cls,id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'_id': id})
        return cls(**blog_data)



