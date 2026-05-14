# 🌧️ Rainfall Prediction Model

A machine learning project that predicts next-day rainfall using historical weather data, achieving a Rain Events F1-score of **0.67**.<br>

## 🎯 Model Performance Comparison

<a href="rainfall-prediction-model.ipynb">
  <img src="images/rainfall-score-table.png" alt="Model Performance Table" width="60%">
</a>
<br>

**Key Insight:** While global metrics like Average Precision are competitive across the two top models, **XGBoost** is the superior choice for stakeholders. By successfully addressing class imbalance through KNN imputation and targeted sampling, it provides a **46%** improvement in Recall for rain events over the Random Forest model (0.52 vs. 0.76), making it the most actionable and dependable tool for rainfall prediction in the Melbourne area.

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
    - Filtered the data for target geographical area.
3. Data Imputation
    - Used KNN imputation to address missing data for features sunshine and cloud cover
4. Feature Engineering
    - Created and refined features to improve model performance
    - Prepared data for machine learning pipelines
5. Modeling
    - Implemented and compared multiple classification models:
        - Logistic Regression
        - Support Vector Machine (SVM)
        - Random Forest
        - XGBoost
    - Used:
        - Scikit-learn Pipelines
        - Stratified K-Fold Cross-Validation

## 📈 Results
* Best model achieved:
    - Overall F1-score: 0.76
    - Rain Event F1-Score: 0.67
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
* README.md                         # Project overview

## 🚀 Future Improvements
* Implement advanced imputation strategies by using Iterative Imputation or KNN Imputation to recover valuable data currently lost through row deletion
* Explore additional feature engineering (lag variables, rolling averages)
* Evaluate additional models and ensemble techniques
