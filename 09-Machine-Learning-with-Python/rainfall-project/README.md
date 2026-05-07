# 🌧️ Rainfall Prediction Model

A machine learning project that predicts next-day rainfall using historical weather data, achieving an F1-score of **0.76**.

## 🔗 Related Notebook
[View Full Analysis Notebook](./rainfall-prediction-model.ipynb)

---

## 📌 Objective

The goal of this project is to develop a classification model that can accurately predict rainfall events, with a focus on handling class imbalance and evaluating model performance using appropriate metrics.

## 📊 Dataset
* Source: Melbourne weather dataset (historical observations)
* Features include:
    - Temperature
    - Humidity
    - Pressure
    - Wind direction and speed
    - Rainfall indicators

## 🔍 Approach

The project follows an end-to-end data science workflow:

1. Data Preparation
    - Data cleaning and preprocessing
    - Handling missing values
    - Feature selection and transformation
2. Exploratory Data Analysis (EDA)
    - Identified key relationships between weather variables and rainfall
    - Visualized distributions and correlations
3. Feature Engineering
    - Created and refined features to improve model performance
    - Prepared data for machine learning pipelines
4. Modeling
    - Implemented and compared multiple classification models:
        - Logistic Regression
        - Support Vector Machine (SVM)
        - Random Forest
    - Used:
        - Scikit-learn Pipelines
        - Stratified K-Fold Cross-Validation

## 📈 Results
* Best model achieved:
    - F1-score: 0.76
* Metric selection focused on F1-score to account for class imbalance in rainfall events

## 🧠 Key Takeaways
* Class imbalance significantly impacts rainfall prediction and requires careful metric selection
* Ensemble methods and proper preprocessing improve predictive performance
* Cross-validation is essential for reliable model evaluation

## 🛠️ Technologies Used
* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Jupyter Notebook

## 📁 Repository Structure
* rainfall-prediction-model.ipynb   # Main notebook with full workflow
* rainfall-readme.md                # Project overview

## 🚀 Future Improvements
* Implement advanced imputation strategies for missing data
* Explore additional feature engineering (lag variables, rolling averages)
* Evaluate additional models and ensemble techniques

