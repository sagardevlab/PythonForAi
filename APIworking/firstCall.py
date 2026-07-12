# import requests libraries, which we can use to interact with apis

import requests

latitude = 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()

temperature = data["current"]["temperature_2m"]