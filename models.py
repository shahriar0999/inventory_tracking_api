from database import Base
from sqlalchemy import Column, Integer, String, Boolean, func, TIMESTAMP, ForeignKey


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    reorder_level = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

class Inventory(Base):
    __tablename__ = "inventory_transactions"

    id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, nullable=False, ForeignKey("products.id", ondelete="CASCADE"))
    quantity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
