from typing import TYPE_CHECKING

from base import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .item import Item # noqa: F401
    """ # noqa: F401 的注释目的是让python解释器忽略可能产生的F401错误 """

class User(Base):
    id = Column(Integer, primary_key=True, index=True) 
    full_name = Column(String, index=True)
    email =  Column(string,unique=True, index=True,nullable=False)
    hashed_password= Column(String,nullable=False)
    is_activate= Column(Boolean(),default=True)
    is_superuser= Column(Boolean(),default=False)
    items= relationship("Item",back_populates="owner")

