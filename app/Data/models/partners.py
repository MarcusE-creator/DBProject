from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base


class Partner(Base):

    __tablename__ = "partners"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    street_address = Column(String(100), nullable=False)
    zip_code = Column(String(10), nullable=False)
    city = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(100), nullable=True)

    contact_person_id = Column(Integer, ForeignKey('contact_persons.id', ondelete='Set Null', onupdate='Cascade'))
    partner_type_id = Column(Integer, ForeignKey('partner_types.id', ondelete='Restrict', onupdate='Cascade'))

    partner_type = relationship('PartnerType', back_populates='partners')
    contact_person = relationship('ContactPerson', back_populates='partners')

    def __repr__(self):
        pass
