from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tariff(Base):
    __tablename__ = 'tariffs'

    id = Column(Integer, primary_key=True, index=True)
    cargo_type = Column(String, index=True)
    rate = Column(Float)
    effective_date = Column(Date)
