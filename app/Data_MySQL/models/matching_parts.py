from ..db import Base
from sqlalchemy import Column, Integer, ForeignKey, Table

matching_parts = Table(
    'matching_parts',
    Base.metadata,
    Column('product_id', Integer, ForeignKey("products.id", ondelete="Cascade", onupdate="Cascade"), primary_key=True),
    Column('car_model_id', Integer, ForeignKey("car_models.id", ondelete="Cascade", onupdate="Cascade"), primary_key=True),
)