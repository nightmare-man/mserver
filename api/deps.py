from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import Depends, HTTPException, status
oa=OAuth2PasswordBearer(tokenUrl="/login")
def get_current_user(token:str=Depends(oa)):
    try:
        payload=jwt.decode(token,"secret_key",algorithms="HS256")
    except (jwt.JWTError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )
    user= payload["user"]
    return user
