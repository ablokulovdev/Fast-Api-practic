from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    Boolean,
    DateTime
)

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    category = Column(String(50))
    brand = Column(String(50))
    price = Column(Float)
    currency = Column(String(50))
    quantity_in_stock = Column(Integer)
    is_active = Column(Boolean)
    discount_percent = Column(Integer)
    rating = Column(Float)
    
    created_at = Column(DateTime)
    updated_at = Column(DateTime)