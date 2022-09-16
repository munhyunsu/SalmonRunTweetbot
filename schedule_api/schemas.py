import datetime

from pydantic import BaseModel


class SalmonrunBase(BaseModel):
    timestart: int
    timeend: int
    stage: str
    weapon1 : str
    weapon2 : str
    weapon3 : str
    weapon4 : str


class SalmonrunCreate(SalmonrunBase):
    pass


class Salmonrun(SalmonrunBase):
    iso8601start: datetime.datetime
    iso8601end: datetime.datetime

    class Config:
        orm_mode = True

