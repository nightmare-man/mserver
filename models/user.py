from base import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email =  Column(string,unique=True, index=True,nullable=False)
    hashed_password= Column(String,nullable=False)
    is_activate= Column(Boolean(),default=True)
    is_superuser= Column(Boolean(),default=False)
    items= relationship("Item",back_populates="owner")

