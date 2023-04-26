from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import Depends, HTTPException, status
oa=OAuth2PasswordBearer(tokenUrl="/login")
def get_current_user(token:str=Depends(oa)):
    print(token)
