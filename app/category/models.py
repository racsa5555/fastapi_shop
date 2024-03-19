from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer,primary_key = True)
    name = Column(String,unique = True)

    products = relationship('Products',back_populates='category',uselist=True)
