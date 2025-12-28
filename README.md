# Used Car Price Prediction (Heroku, Python, PowerBI)

This project focuses on creating interactive visualizations and a prediction model to analyze the relationship between the price of pre-owned cars and various factors such as brand, condition, mileage, location, and more.

## Project Overview
The project is divided into two main parts:

### 1. Interactive Visualization
- Built an **interactive Power BI dashboard** to explore trends and patterns in the used car market.
- Visualizations help understand how features like manufacturer, condition, mileage, and location affect car prices.
- Enables dynamic filtering and drill-down analysis for better insights.

⚠️ **Note:** Currently, the PowerBI dashboard cannot be accessed publicly due to permission and licensing restrictions.


### 2. Price Prediction Model
- Developed a **regression-based machine learning model** using **Python and PySpark**.
- The model predicts used car prices based on selected vehicle attributes.
- Deployed the model using **Flask** and hosted on **Heroku** for real-time inference via a web interface.
![frontend](https://github.com/palak-j/Heroku_Used_Car_Price_Prediction/blob/main/static/frontend_index.png)


## Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data) (Open-source used car dataset) 
- **Original Size:** ~400,000 records, 26 features
- **Final Dataset (after cleaning & preprocessing):**
  - **Records:** ~240,000
  - **Features:** 11
 
### Selected Features
- Car ID  
- City  
- State  
- Manufacturer  
- Model  
- Condition  
- Title Status  
- Odometer  
- Size  
- Car Type  
- Posted Date


## Tech Stack
- **Programming Language:** Python
- **Big Data Processing:** PySpark
- **Machine Learning:** Regression models
- **Visualization:** Power BI
- **Backend:** Flask
- **Deployment:** Heroku


## Model Performance
The trained regression model achieved strong predictive performance:

- **R² Score (Test Data):** `0.999324`
    

## Key Highlights
- End-to-end ML pipeline: data preprocessing → modeling → deployment
- Scalable data handling using PySpark
- Business-driven insights through interactive dashboards
- Real-time price prediction via a deployed web application


## Possible Future Improvements 
- Feature engineering for temporal and seasonal price trends
- Model benchmarking against ensemble methods
- Cloud-based deployment (AWS / GCP)
- Automated retraining pipelines
- Uncertainty estimation for predictions
