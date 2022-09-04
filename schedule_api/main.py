import time
from typing import Union

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
import config
import information


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
  title=information.title,
  description=information.description,
  version=information.version,
  contact=information.contact,
  license_info=information.license_info,
  root_path=config.root_path)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event('startup')
def startup_event():
    pass


@app.on_event('shutdown')
def shutdown_event():
    pass


@app.post('/salmonrun/', response_model=schemas.Salmonrun)
def create_salmonrun(salmonrun: schemas.SalmonrunCreate, api_key: str, db: Session = Depends(get_db)):
    if api_key != config.api_key:
        raise HTTPException(status_code=403, detail='API not authorized')
    db_salmonrun = crud.get_salmonrun_by_timestart(db, timestart=salmonrun.timestart)
    if db_salmonrun:
        raise HTTPException(status_code=404, detail='timestart already registered')
    return crud.create_salmonrun(db=db, salmonrun=salmonrun)


@app.get('/salmonrun/', response_model=list[schemas.Salmonrun])
def read_salmonruns(timequery: Union[int, None] = None, db: Session = Depends(get_db)):
    if timequery is None:
        timequery = int(time.time())
    salmonruns = crud.get_salmonruns(db, timequery=timequery)
    return salmonruns

