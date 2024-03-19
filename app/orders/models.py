from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,Mapped,mapped_column

from app.database import Base

class OrderItem(Base):
    __tablename__ = 'order_items'

    id: Mapped[int] = mapped_column(primary_key=True)
    product: Mapped[int] = mapped_column(ForeignKey('products.id',ondelete='CASCADE'))
    quantity: Mapped[int]
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id',ondelete='CASCADE'))
    
    order: Mapped[int] = relationship('Order',back_populates='items')
        
class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id',ondelete='CASCADE'))
    totalsum: Mapped[Optional[int]]
    address: Mapped[str]
    status: Mapped[str] = mapped_column(default='in processing')
    
    items: Mapped[List[OrderItem]] = relationship('OrderItem',back_populates='order',uselist = True,cascade='all, delete-orphan')
    owner:Mapped[int] = relationship('Users', back_populates='orders',uselist = False)
    




    