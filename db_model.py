from sqlalchemy import Column, Integer, String;
from sqlalchemy.ext.declarative import declarative_base;

Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    totalCost = Column(Integer)
    category = Column(String)
    email = Column(String)
    description = Column(String)
    completed = Column(bool)