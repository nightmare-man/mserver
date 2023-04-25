import uvicorn  
from fastapi import FastAPI  
app=FastAPI()
@app.get("/healthy")
async def healthy():
    return "I am ok!"
if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=9099)
