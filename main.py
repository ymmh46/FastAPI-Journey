from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'hey'

@app.get('/blog/unpublished')
def unpublished():
    return 'unpublished'

@app.get("/blog/{id}")
def show_blog(id):
    return id
