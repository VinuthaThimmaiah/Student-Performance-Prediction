# 🎓 Student Performance Prediction

 Project Overview:
This project predicts student exam performance based on various factors such as study hours, previous scores, sleep, and extracurricular activities using Machine Learning models.

Features:
* Data preprocessing and feature engineering
* Model training using:
  * Linear Regression
  * Random Forest Regressor
* Model evaluation using R² Score
* Interactive web app using Streamlit

Input Features:
* Hours Studied
* Previous Scores
* Extracurricular Activities (Yes/No)
* Sleep Hours
* Sample Papers Practiced
  
Model Performance:
| Model             | R² Score |
| ----------------- | -------- |
| Linear Regression | 0.9889   |
| Random Forest     | 0.9867   |
Linear Regression performed slightly better and was selected as the final model.

Tech Stack:
* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit

How to Run:
pip install -r requirements.txt
streamlit run app.py

Project Structure:
Student-Performance-Prediction/
│── app/
│── models/
│── data/
│── notebooks/
│── README.md

 Future Improvements:
* Deploy app online (Streamlit Cloud)
* Add more features for better prediction
* Use advanced models like XGBoost

 Author-
Vinutha Thimmaiah
