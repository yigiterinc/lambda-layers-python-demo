from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db_commons.model import Base

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    addresses = relationship('Address', backref='person', lazy=True)
