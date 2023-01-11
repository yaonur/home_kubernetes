from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"hy": "ss"}

@app.get('/about')
def about():
    return {"data":{"description":"us us us"}}
