from fastapi import FastAPI, Query
from request import search_species  # import your function

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello Python"}

@app.get("/species")
def get_species(search: str = Query(...)):
    results = search_species(search)
    return {"data": results}