# api/main.py
from fastapi import FastAPI

app = FastAPI(title="Mi API de Scraping")

@app.get("/")
def read_root():
    return {"message": "API funcionando"}
pip install fastapi uvicorn
uvicorn api.main:app --reload
