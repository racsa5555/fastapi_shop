from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Products(Base):

    __tablename__ = 'products'

    id = Column(Integer,primary_key=True)
    title = Column(String)
    description = Column(String,nullable = True)
    price = Column(Integer,nullable = False)
    image_id = Column(String)
    quantity = Column(Integer,nullable = False)
    status = Column(String)
    category_id = Column(Integer,ForeignKey('category.id'))

    category = relationship('Category',back_populates='products',uselist = False)


