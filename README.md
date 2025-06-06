# Weather & Gemini FastAPI Service

This project provides a FastAPI-based web service that integrates with the Google Gemini API for content generation and the WeatherAPI for fetching current weather data. It also summarizes weather information using AI.

## Features

- **/ (GET):** Returns a greeting based on the `condition` query parameter.
- **/weather (POST):** Fetches current weather details for given locations.
- **/info (POST):** Summarizes weather details using Gemini AI.

## Project Structure

- [`main.py`](main.py): FastAPI application with all endpoints.
- [`funtions.py`](funtions.py): Functions for interacting with Gemini and Weather APIs.
- [`schemas.py`](schemas.py): Pydantic models for request payloads.
- `.env`: Stores API keys for Gemini and WeatherAPI.

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd weather
   ```

2. **Install dependencies:**
   ```sh
   pip install fastapi uvicorn pydantic requests python-dotenv
   ```

3. **Configure API keys:**
   - Edit the `.env` file with your Gemini and WeatherAPI keys.

4. **Run the server:**
   ```sh
   uvicorn main:app --reload
   ```

## Example Requests

### Get Greeting

```sh
curl "http://127.0.0.1:8000/?condition=1"
```

### Get Weather

```sh
curl -X POST "http://127.0.0.1:8000/weather" -H "Content-Type: application/json" -d '{"locations":[{"q":"London"}]}'
```

### Get Weather Summary

```sh
curl -X POST "http://127.0.0.1:8000/info" -H "Content-Type: application/json" -d '{"locations":[{"q":"London"}]}'
```

for the location "Trivandrum" the response body for "info" is as follows:
![image](https://github.com/user-attachments/assets/f74a7cfe-216f-4dda-91bc-108a06570e4a)

