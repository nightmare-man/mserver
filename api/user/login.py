from typing import Any
from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import 

router=APIRouter(prefix="/user", tags=["user"])

@routet.post("/create")
