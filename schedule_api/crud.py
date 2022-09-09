from sqlalchemy.orm import Session

import models, schemas


def get_salmonruns(db: Session, timequery: int):
    return db.query(models.Salmonrun).filter(models.Salmonrun.timeend > timequery).order_by(models.Salmonrun.timestart.asc()).all()


def get_salmonrun_by_timestart(db: Session, timestart: int):
    return db.query(models.Salmonrun).filter(models.Salmonrun.timestart == timestart).first()


def create_salmonrun(db: Session, salmonrun: schemas.SalmonrunCreate):
    db_salmonrun = models.Salmonrun(**salmonrun.dict())
    db.add(db_salmonrun)
    db.commit()
    db.refresh(db_salmonrun)
    return db_salmonrun


def update_salmonrun(db: Session, salmonrun: schemas.SalmonrunCreate):
    db_salmonrun = db.query(models.Salmonrun).filter(models.Salmonrun.timestart == salmonrun.timestart).first()
    db_salmonrun.timeend = salmonrun.timeend
    db_salmonrun.stage = salmonrun.stage
    db_salmonrun.weapon1 = salmonrun.weapon1
    db_salmonrun.weapon2 = salmonrun.weapon2
    db_salmonrun.weapon3 = salmonrun.weapon3
    db_salmonrun.weapon4 = salmonrun.weapon4
    db.commit()
    db.refresh(db_salmonrun)
    return db_salmonrun
