from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)  # PRIMARY KEY
    store_id = Column(Integer, ForeignKey('stores.id', ondelete="Restrict", onupdate="Cascade"), nullable=False)  # FOREIGN KEY --> Stores

    name = Column(String(100), nullable=False)
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)
    job_title = Column(String(45), nullable=False)

    store = relationship('Store', back_populates='employees')

    def __repr__(self):
        pass
