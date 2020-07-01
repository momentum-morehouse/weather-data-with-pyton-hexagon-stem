import requests

place_list = []

def get_weather_data(place_list):


url = "https://api.climacell.co/v3/weather/realtime"
payload = {
  "apikey": "MlzJxYVk8vU6tjV0U4SNf9WKItn4fTzq","lat":35.7767, 
  "lon":140.3187,
  "fields": ["temp", "precipitation", "wind_gust"],
  "unit_system":"us", 

   }

response = requests.get(url, params=payload).json()

print(response)