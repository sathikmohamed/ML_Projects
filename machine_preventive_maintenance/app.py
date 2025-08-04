from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    # Render form with no result on initial load
    return render_template('home.html', results=None)

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html', results=None)
    else:
        data = CustomData(
            Temperature = float(request.form.get('temperature')),
            Vibration = float(request.form.get('vibration')),
            Pressure = float(request.form.get('pressure')),
            Voltage = float(request.form.get('voltage')),
            Current = float(request.form.get('current')),
            FFT_Feature1 = float(request.form.get('fft_feature1')),
            FFT_Feature2 = float(request.form.get('fft_feature2')),
            Normalized_Temp = float(request.form.get('normalized_temp')),
            Normalized_Vibration = float(request.form.get('normalized_vibration')),
            Normalized_Pressure = float(request.form.get('normalized_pressure')),
            Normalized_Voltage = float(request.form.get('normalized_voltage')),
            Normalized_Current = float(request.form.get('normalized_current')),
            Anomaly_Score = float(request.form.get('anomaly_score')),
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        # Show prediction result
        return render_template('home.html', results=result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
