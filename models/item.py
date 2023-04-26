from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User #noqa: F401

class Item(Base):
    id = Column(Integer, primary_key=True, index=True )
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeginKey("user.id"))
    """ 通过relationship来实现 item.owner访问对应的用户
        back_populates是指的user.items指向 item
        反向访问
    """
    owner = relationship("User", back_populates="items")
