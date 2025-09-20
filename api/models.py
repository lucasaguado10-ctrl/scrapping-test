from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class SerieEconomica(Base):
    __tablename__ = "series_economicas"
    id = Column(Integer, primary_key=True, index=True)
    indicador = Column(String, index=True)   # ej: "riesgo_pais"
    fecha = Column(Date, default=datetime.date.today, index=True)
    valor = Column(Float)
