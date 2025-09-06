import joblib
import numpy as np
from config.paths_config import MODEL_OUTPUT_PATH
from flask import Flask, render_template, request

app = Flask(__name__)

# Try to load model; don't crash if missing
try:
    loaded_model = joblib.load(MODEL_OUTPUT_PATH)
except Exception as e:
    loaded_model = None
    print(f"Warning: Could not load model from {MODEL_OUTPUT_PATH}: {e}")

@app.route('/health')
def health():
    return {"status": "ok", "model_loaded": loaded_model is not None}, 200

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lead_time = int(request.form["lead_time"])
        no_of_special_request = int(request.form["no_of_special_request"])
        avg_price_per_room = float(request.form["avg_price_per_room"])
        arrival_month = int(request.form["arrival_month"])
        arrival_date = int(request.form["arrival_date"])

        market_segment_type = int(request.form["market_segment_type"])
        no_of_week_nights = int(request.form["no_of_week_nights"])
        no_of_weekend_nights = int(request.form["no_of_weekend_nights"])

        type_of_meal_plan = int(request.form["type_of_meal_plan"])
        room_type_reserved = int(request.form["room_type_reserved"])

        features = np.array([[
            lead_time,
            no_of_special_request,
            avg_price_per_room,
            arrival_month,
            arrival_date,
            market_segment_type,
            no_of_week_nights,
            no_of_weekend_nights,
            type_of_meal_plan,
            room_type_reserved
        ]])

        if loaded_model is None:
            return render_template('index.html', prediction="Model not loaded. Please train or place model.joblib.")

        prediction = loaded_model.predict(features)
        return render_template('index.html', prediction=prediction[0])

    return render_template('index.html', prediction=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
