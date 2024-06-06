import requests
from datetime import datetime, timedelta

class WeatherAPI:
    def __init__(self, api_key, location):
        self.api_key = api_key
        self.location = location
        self.base_url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"

    def generate_urls(self, years_back=6):
        urls = []
        current_year = datetime.now().year

        for year in range(current_year - years_back, current_year):
            for month in range(1, 13):
                start_date = datetime(year, month, 1)
                if month == 12:
                    end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
                else:
                    end_date = datetime(year, month + 1, 1) - timedelta(days=1)
                
                start_date_str = start_date.strftime('%Y-%m-%d')
                end_date_str = end_date.strftime('%Y-%m-%d')
                
                url = f"{self.base_url}?key={self.api_key}&q={self.location}&format=json&date={start_date_str}&enddate={end_date_str}&tp=24"
                urls.append(url)

        return urls

    def get_weather_data(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def extract_weather_data(self, weather_data):
        extracted_data = []
        
        for day in weather_data:
            date = day["date"]
            avgtempC = day["avgtempC"]
            
            extracted_data.append({
                "date": date,
                "avgtempC": avgtempC,
            })
        
        return extracted_data
