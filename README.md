# ⚽ ScoreSight Prediction System

ScoreSight is a Machine Learning–based football analytics application built using Python and Streamlit.  
It focuses on player performance prediction and provides a foundation for match outcome prediction using English Premier League (EPL) data.

🔗 Live App (Streamlit Cloud):  
(https://epl-scoresight-prediction-system-jztoswxkywysrybqjlnrn6.streamlit.app/)

---

## 🚀 Project Overview

The ScoreSight Prediction System analyzes EPL player statistics and applies supervised machine learning models to generate meaningful predictions.

The application is designed to be interactive, simple to use, and deployable on the cloud.

---

## 🧠 Machine Learning Models Used

| Task | Model |
|----|----|
| Player Goal Prediction | Linear Regression |
| Player Performance Classification | Logistic Regression |
| Feature Scaling | StandardScaler |

---

## 📊 Dataset Description

The dataset used in this project is a **player-level EPL dataset** containing detailed performance statistics such as:

- Age  
- Appearances  
- Goals  
- Assists  
- Shots & Shots on Target  
- Shooting Accuracy (%)  
- Passes per match  
- Big chances created  
- Defensive and disciplinary metrics  

Percentage-based columns are cleaned and converted into numerical format during preprocessing.

---

## 🧱 Project Structure

EPL-scoresight-prediction-system/
│
├── app.py # Streamlit application
├── train_model.py # ML training and preprocessing logic
├── epl_players.csv # EPL player dataset
├── requirements.txt # Project dependencies
├── README.md # Project documentation

yaml
Copy code

---

## 🖥️ Application Features

### 🏟️ Match Prediction (UI Ready)
- Home team vs Away team selection
- Match outcome prediction interface
- Designed for future ML-based match result integration

### 🧑‍💼 Player Prediction
- Select any EPL player
- Predict expected goal output
- Classify player performance as High or Average

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
git clone https://github.com/Hitanshu480/EPL-scoresight-prediction-system.git
cd EPL-scoresight-prediction-system

shell
Copy code

### 2️⃣ Install dependencies
pip install -r requirements.txt

graphql
Copy code

### 3️⃣ Run the Streamlit app
streamlit run app.py

yaml
Copy code

---

## ☁️ Deployment

The application is deployed using Streamlit Cloud with GitHub integration.

Deployment steps:
1. Push the project to GitHub
2. Connect the repository on Streamlit Cloud
3. Select `app.py` as the main file
4. Deploy the application

---

## 🧠 Learning Outcomes

- Data cleaning and preprocessing of real-world datasets
- Handling percentage and mixed-type features
- Applying regression and classification models
- Building interactive ML applications with Streamlit
- Git and GitHub version control workflow
- Cloud deployment using Streamlit Cloud

---

## 🔮 Future Enhancements

- Win / Draw / Loss probability prediction
- Team strength modeling using player aggregation
- Advanced ML models (Poisson, XGBoost)
- Player vs Player comparison
- Interactive charts and dashboards

---

## 👨‍💻 Author

Hitanshu Sekhar Das  
MCA | Data Analytics & Machine Learning  
GitHub: https://github.com/Hitanshu480  

---

## 📜 License

This project is intended for educational and learning purposes only.
