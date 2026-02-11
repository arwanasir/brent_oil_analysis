from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

prices_df = pd.read_csv('../../data/raw/BrentOilPrices.csv')
prices_df['Date'] = pd.to_datetime(prices_df['Date'])
events_df = pd.read_csv('../../data/processed/researched_events.csv')


@app.route('/api/historical-prices', methods=['GET'])
def get_historical_prices():
    data = prices_df.copy()
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
    return jsonify(data.to_dict(orient='records'))


@app.route('/api/events', methods=['GET'])
def get_events():
    return jsonify(events_df.to_dict(orient='records'))


@app.route('/api/analysis-results', methods=['GET'])
def get_analysis():
    results = {
        "total_events": len(events_df),
        "avg_price": prices_df['Price'].mean(),
        "volatility": prices_df['Price'].std()
    }
    return jsonify(results)


@app.route('/api/change-points', methods=['GET'])
def get_change_points():
    change_points = [
        {"date": "2008-07-11", "label": "2008 Peak", "impact": "-38%"},
        {"date": "2014-11-27", "label": "OPEC Crash", "impact": "-40%"},
        {"date": "2020-03-09", "label": "COVID/Price War", "impact": "-25%"}
    ]
    return jsonify(change_points)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
