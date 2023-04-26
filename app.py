import uvicorn 
from typing import Any
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.deps import get_current_user
app=FastAPI()
@app.get("/healthy")
async def healthy(user:Any = Depends(get_current_user)):
    return "I am ok!"
@app.post("/login")
async def login( form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username)
    print(form_data.password)

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=9099)
