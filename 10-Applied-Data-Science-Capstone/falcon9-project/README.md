# 🚀 Falcon 9 First-Stage Landing Predictor

This project analyzes historical SpaceX launch data to predict whether the Falcon 9 first-stage booster will successfully land after launch. The project combines data collection, exploratory data analysis (EDA), feature engineering, machine learning classification, and interactive visualizations to support predictive modeling and operational insights.

The analysis was completed as part of the IBM Data Science Professional Certificate program.

## 🔗 Related Notebooks and Dashboard Code

### 1. Data Collection & Wrangling
   - [Data Collection via SpaceX API](./notebooks/n01_spacex-data-collection-api.ipynb)
   - [Web Scraping from Wikipedia](./notebooks/n02_spacex_data_collection_webscraping.ipynb)
   - [Data Wrangling and Cleaning](./notebooks/n03_spacex_data_wrangling.ipynb)

### 2. Exploratory Data Analysis (EDA)
   - [EDA with SQL](./notebooks/n04_spacex_eda_sql.ipynb)
   - [EDA with Visualization (Pandas/Matplotlib)](./notebooks/n05_spacex_eda_visualizations.ipynb)

### 3. Interactive Visual Analytics
   - [Geospatial Analysis with Folium](./notebooks/n06_spacex_launch_site_locations.ipynb)
   - [Interactive Dashboard with Plotly Dash](./dashboard/spacex-dash-app.py)

### 4. Machine Learning & Prediction
   - [Machine Learning Prediction & Model Evaluation](./notebooks/n07_spacex_machine_learning_prediction.ipynb)

---

## 📌 Objectives

*	Collect and integrate launch data from multiple sources
*	Perform exploratory data analysis using SQL and Python
*	Engineer features relevant to landing success prediction
*	Build and evaluate classification models
*	Visualize launch site and booster landing trends
*	Develop an interactive dashboard for data exploration

## 📊 Dataset
* Source: SpaceX and Wikipedia
* Features include:
    - Launch Date
    - Flight Number
    - Booster Version
    - Launch Site
    - Payload Mass
    - Outcome

## 🔍 Approach

The project follows an end-to-end data science workflow:

#### 1. Data Collection
    Data was collected from:
    
    • SpaceX REST API
    • Wikipedia web scraping using BeautifulSoup

    The datasets were cleaned and combined into a unified analytical dataset.
    
#### 2. Exploratory Data Analysis (EDA) 
    EDA was performed using: 
    
    • SQL queries
    • Python data analysis libraries
    • Statistical summaries
    • Data visualizations 

    Key patterns analyzed included: 
    
    • Launch site performance
    • Payload mass distributions
    • Booster version trends
    • Orbit classifications
    • Launch success rates

#### 3. Feature Engineering 
    Features were prepared for machine learning through: 
    
    • Categorical encoding
    • Data normalization
    • Missing value handling
    • Feature selection

#### 4. Machine Learning Modeling 
    Multiple classification algorithms were evaluated: 
    
    • Logistic Regression
    • Support Vector Machine (SVM)
    • Nearest Neighbors (KNN)
    • Decision Tree

    Models were trained and validated using cross-validation techniques.

    Top-performing models achieved: 
    
    • 0.83 accuracy on the test set

#### 5. Visualization and Dashboarding 
    The project includes:
    
    • Geospatial launch analysis using Folium
    • Interactive visualizations using Plotly
    • A Plotly Dash dashboard for dynamic data exploration

## 📈 Results

*	Built an end-to-end machine learning workflow for launch outcome prediction
*	Integrated API and web-scraped datasets into a unified pipeline
*	Achieved strong predictive performance with multiple classification models
*	Developed interactive dashboards and geospatial visualizations to communicate findings

## 🧠 Key Takeaways
* Small dataset due to the nature of the business case
* Cross-validation is necessary for proper model evaluation

## 🛠️ Technologies Used
*	Python
*	Pandas
*	NumPy
*	Scikit-learn
*	SQL
*	Plotly Dash
*	Folium
*	Matplotlib
*	Seaborn
*	BeautifulSoup
*	SpaceX REST API
*	Jupyter Notebook

## 📁 Repository Structure

```text
falcon9-project/
├── dashboard/              # Python application with Plotly Dash
│   ├── spacex-dash-app.py
├── data/                   # SpaceX API & Wikipedia scraped datasets
├── images/                 # Visualizations
├── notebooks/              # End-to-end Jupyter Notebooks
│   ├── n01_spacex-data-collection-api.ipynb
│   ├── n02_spacex_data_collection_webscraping.ipynb
│   ├── n03_spacex_data_wrangling.ipynb
│   ├── n04_spacex_eda_sql.ipynb
│   ├── n05_spacex_eda_visualizations.ipynb
│   ├── n06_spacex_launch_site_locations.ipynb
│   └── n07_spacex_machine_learning_prediction.ipynb
└── README.md               # Project documentation and summary
```

## 🚀 Future Improvements
*	Hyperparameter optimization
*	Additional feature engineering
*	Deployment as a standalone web application
*	Expanded launch dataset updates
*	Advanced ensemble modeling
