import pandas as pd
from Work.weather_api import WeatherAPI

# Nasz klucz oraz wybrana lokalizacja
api_key = "4597174352ee463084a193409241305"
location = "London"

# Inicjalizacja API
weather_api = WeatherAPI(api_key, location)

# Generowanie URL
urls = weather_api.generate_urls()

# Pobieranie i przetwarzanie danych
all_weather_data = []

for url in urls:
    data = weather_api.get_weather_data(url)
    weather_data = data["data"]["weather"]
    avg_temps = weather_api.extract_weather_data(weather_data)
    all_weather_data.extend(avg_temps)

# Tworzenie DataFrame
df = pd.DataFrame({"avgtempC": all_weather_data})
print(df)
