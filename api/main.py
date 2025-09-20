from fastapi import FastAPI
from .database import engine, SessionLocal
from .models import Base, SerieEconomica
from .scraper import get_riesgo_pais
import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi API de Scraping")

@app.get("/")
def read_root():
    return {"message": "API funcionando"}

@app.post("/scrape/riesgo-pais")
def scrape_riesgo_pais():
    session = SessionLocal()
    valor = get_riesgo_pais()
    registro = SerieEconomica(
        indicador="riesgo_pais",
        fecha=datetime.date.today(),
        valor=valor
    )
    session.add(registro)
    session.commit()
    session.close()
    return {"status": "ok", "valor": valor}

