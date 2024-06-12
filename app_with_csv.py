from flask import Flask, jsonify, render_template
import pandas as pd
from datetime import datetime
import pmdarima as pm
from sklearn.metrics import mean_squared_error
import pmdarima as pm
import os
import logging
import pickle

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Wczytywanie danych
file_path = os.path.join('Data', 'weather_data.csv')
df = pd.read_csv(file_path)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['avgtempC'] = df['avgtempC'].astype(int)
temp_df = df['avgtempC']
test_df = temp_df['2023':'2024'].resample('M').mean()

# Wczytywanie modelu
model_file_path = '/app/Models/weather_forecast_model.pkl'
with open(model_file_path, 'rb') as model_file:
    model = pickle.load(model_file)
app.logger.debug(f"Model wczytany z {model_file_path}")


@app.route('/weather_forecast', methods=['GET'])
def weather_forecast():          
        forecast = model.predict(n_periods=len(test_df))
        forecast = pd.DataFrame(forecast, index=test_df.index, columns=['Prediction'])

        error = mean_squared_error(test_df, forecast)
        
        forecast.index = forecast.index.strftime('%Y-%m-%d')
        
        forecast_dict = {date: {'Prediction': row['Prediction']} for date, row in forecast.iterrows()}
        app.logger.debug(f"Restructured Forecast dictionary: {forecast_dict}")
    
        return render_template('forecast.html', error=error, forecast=forecast_dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

