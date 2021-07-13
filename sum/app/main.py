# to test this locally, run "uvicorn main:app --reload" in the same folder
from typing import List, Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class params_sum_two(BaseModel):
     a: int
     b: int

@app.post("/two")
async def sum_two(p:params_sum_two):
     return p.a + p.b


class params_sum_more(BaseModel):
     l: List[int]

@app.post("/more")
async def sum_more(p:params_sum_more):
     return sum(p.l)
