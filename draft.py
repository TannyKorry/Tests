import requests
from pprint import pprint

class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)

blog = Blog('Sasha')

if __name__ == '__main__':
    pprint(blog.posts())