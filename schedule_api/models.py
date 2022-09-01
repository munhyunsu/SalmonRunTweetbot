from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Salmonrun(Base):
    __tablename__ = 'salmonrun'

    timestart = Column(Integer, primary_key=True, index=True)
    timeend = Column(Integer, unique=True, index=True)
    stage = Column(String)
    weapon1 = Column(String)
    weapon2 = Column(String)
    weapon3 = Column(String)
    weapon4 = Column(String)

