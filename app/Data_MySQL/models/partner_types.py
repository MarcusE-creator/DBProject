from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..db import Base


class PartnerType(Base):

    __tablename__ = "partner_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)

    partners = relationship('Partner', back_populates='partner_type')

    def __repr__(self):
        pass
