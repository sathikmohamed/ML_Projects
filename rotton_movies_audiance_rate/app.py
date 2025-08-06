from flask import Flask, request, render_template
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
        # Collect input features from the form
        data = CustomData(
            movie_title = request.form.get('movie_title'),
            movie_info = request.form.get('movie_info'),
            critics_consensus = request.form.get('critics_consensus'),
            rating = request.form.get('rating'),
            genre = request.form.get('genre'),
            directors = request.form.get('directors'),
            writers = request.form.get('writers'),
            cast = request.form.get('cast'),
            in_theaters_date = request.form.get('in_theaters_date'),  # expect format 'YYYY-MM-DD'
            on_streaming_date = request.form.get('on_streaming_date'), # expect format 'YYYY-MM-DD'
            runtime_in_minutes = int(request.form.get('runtime_in_minutes')),
            studio_name = request.form.get('studio_name'),
            tomatometer_status = request.form.get('tomatometer_status'),
            tomatometer_rating = int(request.form.get('tomatometer_rating')),
            tomatometer_count = int(request.form.get('tomatometer_count')),
            release_year = int(request.form.get('release_year')),
            movie_age_years = float(request.form.get('movie_age_years')),
            has_critics_consensus = int(request.form.get('has_critics_consensus')),
            primary_genre = request.form.get('primary_genre'),
        )

        # Convert inputs into DataFrame with appropriate preprocessing done inside CustomData
        pred_df = data.get_data_as_data_frame()

        # Load your trained model and do prediction
        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)

        # Return predicted audience rating
        return render_template('home.html', results=result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
