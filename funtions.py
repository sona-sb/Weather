import os
import requests
import schemas
from dotenv import load_dotenv


load_dotenv()
gemini_api= os.getenv("gemini")
weather_api=os.getenv("weather")


#for gemini API
def gemini(content:schemas.Contents):
    response=requests.post(url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_api}",json=content.model_dump())
    response_body=response.json()
    return response_body["candidates"][0]["content"]["parts"][0]["text"]

#for weather API
def weather(locations:schemas.Locations):
    response=requests.post(url=f"http://api.weatherapi.com/v1/current.json?key={weather_api}&q=bulk",json=locations.model_dump())
    response_body=response.json()
    return response_body