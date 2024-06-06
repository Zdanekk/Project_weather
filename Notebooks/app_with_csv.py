from flask import Flask, jsonify
import pandas as pd
from datetime import datetime
import pmdarima as pm
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

df = pd.read_csv("../data/weather_data.csv")

@app.route('/weather_forecast', methods=['GET'])
def weather_forecast():
    try:   
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
        
        forecast.index = forecast.index.strftime('%Y-%m-%d')
        
        result = {
            'Test Mean Squared Error': error,
            'Forecast': forecast.to_dict()
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5005)
