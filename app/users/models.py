from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

from app.orders.models import Order

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer,primary_key = True)
    first_name = Column(String,nullable = False)
    last_name = Column(String,nullable= False)
    email = Column(String,nullable=False,unique = True)
    password = Column(String,nullable = False)
    role = Column(String,nullable = False)

    orders = relationship('Order',back_populates='owner')
    