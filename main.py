from fastapi import FastAPI
from typing import Optional
import schemas
import funtions

app = FastAPI()                                      #instace of FastAPI

@app.get("/")
def read_root(condition: Optional[int] = 1):         # condition: Optional[bool] = True
    if condition==1:
        return "good morning!!!"
    else:
        return "good night!!!"


""""

@app.post("/gemini")                                  #generating content using gemini API 
def gemini(content:schemas.Contents):
    return funtions.gemini(content)

"""

@app.post("/weather")                                 #getting proper weather details of a location
def weather(locations:schemas.Locations):
    return funtions.weather(locations)

@app.post("/info")                                     #summarizing weather info by giving prompt to gemini
def info(locations:schemas.Locations):
    details = funtions.weather(locations)
    prompt = f'based on the following weather details summarize the current weather conditions in 5-6 sentances without sub-headings. mention whether its sunny,cloudy,rainy etc also provide informations about the precautions to be taken while going out. weather details is : {details}'

    request = schemas.Contents(
        contents=[
            schemas.Parts(
                parts=[
                    schemas.Text(text=prompt)
                ]
            )
        ]
    )
    return funtions.gemini(request)


