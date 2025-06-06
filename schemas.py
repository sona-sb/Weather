from pydantic import BaseModel
from typing import List


# PAYLOAD FOR GEMINI

class Text(BaseModel):
    text:str
class Parts(BaseModel):
    parts:List[Text]
class Contents(BaseModel):
    contents:List[Parts]


# PAYLOAD FOR WEATHER

class Q(BaseModel):
    q:str
class Locations(BaseModel):
    locations:List[Q]