# to test this locally, run "uvicorn main:app --reload" in the same folder
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
     return {"message": "Hello World"}
