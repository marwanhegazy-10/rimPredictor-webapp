# RimPredictor Web Application

## Overview
RimPredictor is a machine learning-based NBA game predictor that utilizes web scraping, data processing, and predictive modeling to forecast game outcomes. This web application provides an intuitive interface for users to interact with the underlying functionalities of the RimPredictor project.

## Features
- **Data Scraping**: Automatically fetches NBA game schedules, standings, and box scores using Playwright and BeautifulSoup.
- **Data Processing**: Cleans and structures the scraped data into usable formats for analysis.
- **Game Outcome Prediction**: Utilizes a trained machine learning model to predict the outcomes of NBA games based on historical data.

## Installation Instructions
1. **Clone the repository**:
   ```
   git clone https://github.com/marwanhegazy-10/rimPredictor.git
   cd rimPredictor-webapp
   ```

2. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**:
   ```
   playwright install
   ```

4. **Run the web application**:
   ```
   python src/app.py
   ```

5. **Access the application**: Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage Instructions
- **Scraping Data**: Navigate to the home page and click the button to initiate the scraping process.
- **Processing Data**: After scraping, click the corresponding button to process the data.
- **Predicting Outcomes**: Use the prediction feature to view the outcomes based on the processed data.

## Key Results
The application showcases the prediction accuracy and insights derived from the analysis of NBA game data, providing users with valuable information on game outcomes.