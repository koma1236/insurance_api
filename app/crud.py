from sqlalchemy.orm import Session
from app import models, schemas


def create_tariff(db: Session, tariff: schemas.TariffCreate):
    db_tariff = models.Tariff(**tariff.dict())
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff


def get_tariff(db: Session, cargo_type: str, effective_date):
    return db.query(models.Tariff).filter(models.Tariff.cargo_type == cargo_type,
                                          models.Tariff.effective_date == effective_date).first()
