# to test this locally, run "uvicorn main:app --reload" in the same folder
from fastapi import FastAPI
from os import environ

app = FastAPI(title="Hello World", version="1.0")

@app.get("/")
async def root():
     if environ.get('MESSAGE'):
          return {"message": environ.get('MESSAGE')}
     else:
          return {"message": "Hello World"}
