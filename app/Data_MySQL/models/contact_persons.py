from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base


class ContactPerson(Base):

    __tablename__ = 'contact_persons'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    customer = relationship('Customer', back_populates='contact_person')
    partners = relationship('Partner', back_populates='contact_person')

    def __repr__(self):
        return f"{self.name} ({self.id}) - {self.phone}, {self.email}"
