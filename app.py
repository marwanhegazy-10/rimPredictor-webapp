from flask import Flask, render_template, request, redirect, url_for, flash
from utils.scraper import scrape_data
from utils.data_processor import process_data
from utils.predictor import make_predictions
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        scrape_data()
        flash('Data scraped successfully!', 'success')
    except Exception as e:
        flash(f'Error during scraping: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.route('/process', methods=['POST'])
def process():
    try:
        process_data()
        flash('Data processed successfully!', 'success')
    except Exception as e:
        flash(f'Error during processing: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        predictions = make_predictions()
        return render_template('results.html', predictions=predictions)
    except Exception as e:
        flash(f'Error during prediction: {str(e)}', 'danger')
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)