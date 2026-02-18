from fastapi import FastAPI, Query
from request import search_species  # import your function
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path



app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

@app.get("/hello")
def say_hello():
    return {"message": "Hello Python"}

@app.get("/species")
def get_species(search: str = Query(...)):
    results = search_species(search)
    return {"data": results}

@app.get("/", response_class=FileResponse)
def return_site():
    # Serve the HTL file directly
    return FileResponse(BASE_DIR / "templates" / "index.html", media_type="text/html")