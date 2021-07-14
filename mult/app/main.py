# to test this locally, run "uvicorn main:app --reload" in the same folder
from typing import List, Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel
from math import prod

app = FastAPI()

class params_mult_two(BaseModel):
     a: int
     b: int

@app.post("/two")
async def mult_two(p:params_mult_two):
     return p.a * p.b


class params_mult_more(BaseModel):
     l: List[int]

@app.post("/more")
async def mult_more(p:params_mult_more):
     return prod(p.l)
