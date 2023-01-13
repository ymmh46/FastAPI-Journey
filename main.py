from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return 'hey'

class Blog(BaseModel):
    title: str
    body: str
    published: bool | None = None

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data'  : f"Blog is created with the title as {blog.title}"}
