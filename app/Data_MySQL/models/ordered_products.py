from ..db import Base
from sqlalchemy import Column, Integer, ForeignKey


class OrderedProduct(Base):
    __tablename__ = 'ordered_products'

    order_id = Column(Integer, ForeignKey('orders.id', ondelete="Cascade", onupdate="Cascade"), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete="Restrict", onupdate="Cascade"), primary_key=True)
    product_amount = Column(Integer, nullable=False)

    def __repr__(self):
        pass
