from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import SessionLocal
from app.kafk import log_event

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tariffs/", response_model=schemas.Tariff)
def create_tariff(tariff: schemas.TariffCreate, db: Session = Depends(get_db)):
    log_event(user_id=tariff.user_id, action="create_tariff")
    return crud.create_tariff(db=db, tariff=tariff)


@router.get("/tariffs/{cargo_type}/{effective_date}", response_model=schemas.Tariff)
def read_tariff(cargo_type: str, effective_date: str, db: Session = Depends(get_db)):
    effective_date = date.fromisoformat(effective_date)
    db_tariff = crud.get_tariff(db, cargo_type=cargo_type, effective_date=effective_date)
    if db_tariff is None:
        raise HTTPException(status_code=404, detail="Tariff not found")
    log_event(user_id=db_tariff.user_id, action="read_tariff")
    return db_tariff
