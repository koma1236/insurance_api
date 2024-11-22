from pydantic import BaseModel
from datetime import date


class TariffBase(BaseModel):
    cargo_type: str
    rate: float
    effective_date: date


class TariffCreate(TariffBase):
    pass


class Tariff(TariffBase):
    id: int

    class Config:
        from_attributes = True
