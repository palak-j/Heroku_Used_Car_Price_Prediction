# Used Car Price Prediction (Heroku, Python, PowerBI)

This project focuses on creating interactive visualizations and a prediction model to analyze the relationship between the price of pre-owned cars and various factors such as brand, condition, mileage, location, and more.

## Project Overview
The project is divided into two main parts:

### 1. Interactive Visualization
We utilized Power BI to build an interactive dashboard that provides insights into the dataset. You can view the hosted dashboard here:
markdown
   [Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiN2I0M2UzZjUtNzE4NS00Mjc1LWIzNmEtYThhZGY5MDEyMzQwIiwidCI6IjExMTNiZTM0LWFlZDEtNGQwMC1hYjRiLWNkZDAyNTEwYmU5MSIsImMiOjN9)

### 2. Prediction Model
We developed a machine learning model using Python and PySpark, and deployed it on Heroku via a Flask web application.
![frontend](https://github.com/palak-j/Heroku_Used_Car_Price_Prediction/blob/main/static/frontend_index.png)

## Dataset
The dataset used in this project is an open-source dataset of used cars from [Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data), consisting of 400,000 records and 26 features. After cleaning and preprocessing with Python, the final dataset includes:

Number of Features: 11 <br>
Features: Car ID, City, State, Manufacturer, Model, Condition, Title Status, Odometer, Size, Car Type, Posted Date <br>
Number of Records: 240,000


## Model Performance
For this regression model, R squared value on test set is: <br>
**R Squared (R2) on test data = 0.999324**
