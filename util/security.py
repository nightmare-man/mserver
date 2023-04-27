from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
#用于hash密码和验证hash应用的
from passlib.context import CryptContext
#bcrypt是用于密码的散列函数
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"

def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
        )
