from flask import Flask, jsonify, request
import requests
import pandas as pd
from datetime import datetime, timedelta
import pmdarima as pm
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

def generate_weather_api_urls(api_key, location, years_back=6):
    base_url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx"
    urls = []

    # Pobranie biezacej daty
    current_year = datetime.now().year

    # Pętla z ostatnimi 3 latami
    for year in range(current_year - years_back, current_year):
        for month in range(1, 13):  # zakres od stycznia do grudnia
            # definiowanie dnia startowego i koncowego dla kazdego miesiaca
            start_date = datetime(year, month, 1)
            if month == 12:
                end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
            else:
                end_date = datetime(year, month + 1, 1) - timedelta(days=1)
            
            # Formatowanie daty do 'YYYY-MM-DD'
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')
            
            # Uzupełnianie API
            url = f"{base_url}?key={api_key}&q={location}&format=json&date={start_date_str}&enddate={end_date_str}&tp=24"
            urls.append(url)

    return urls

def extract_weather_data(weather_data):
    extracted_data = []
    
    for day in weather_data:
        date = day["date"]
        maxtempC = day["maxtempC"]
        mintempC = day["mintempC"]
        avgtempC = day["avgtempC"]
        sunHour = day["sunHour"]
        humidity = day["hourly"][0]["humidity"]
        pressure = day["hourly"][0]["pressure"]
        
        extracted_data.append({
            "date": date,
            "maxtempC": maxtempC,
            "mintempC": mintempC,
            "avgtempC": avgtempC,
            "sunHour": sunHour,
            "humidity": humidity,
            "pressure": pressure
        })
    
    return extracted_data


@app.route('/weather_forecast', methods=['GET'])
def weather_forecast():    
    api_key = request.args.get('api_key', '4597174352ee463084a193409241305')
    location = request.args.get('location', 'London')

    urls = generate_weather_api_urls(api_key, location)
    all_weather_data = []

    for url in urls:
        response = requests.get(url)
        data = response.json()
        
        # Sprawdzenie, czy odpowiedź zawiera klucz 'weather'
        if 'data' in data and 'weather' in data['data']:
            weather_data = data["data"]["weather"]
            month_weather_data = extract_weather_data(weather_data)
            all_weather_data.extend(month_weather_data)
        else:
            return jsonify({"error": "Błąd w odpowiedzi API dla URL: {}".format(url)}), 400

    if not all_weather_data:
        return jsonify({"error": "Brak danych pogodowych"}), 400


    df = pd.DataFrame(all_weather_data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['avgtempC'] = df['avgtempC'].astype(int)    
    
    temp_df = df['avgtempC']
    train_df = temp_df['2018':'2022'].resample('M').mean()
    test_df = temp_df['2023':'2024'].resample('M').mean()
    
    model = pm.auto_arima(train_df, seasonal=True, m=12)
    model.fit(train_df)
    forecast = model.predict(n_periods=len(test_df))
    forecast = pd.DataFrame(forecast, index=test_df.index, columns=['Prediction'])
    error = mean_squared_error(test_df, forecast)

    # Konwersja indeksu na str przed zwróceniem jako JSON
    forecast.index = forecast.index.strftime('%Y-%m-%d')
    
    result = {
        'Test Mean Squared Error': error,
        'Forecast': forecast.to_dict()
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5005)

