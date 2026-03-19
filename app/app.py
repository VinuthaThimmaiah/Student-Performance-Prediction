import streamlit as st
import numpy as np
import pickle
import os

# Load model correctly
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "student_model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("🎓 Student Performance Predictor")

hours_studied = st.slider("Hours Studied", 0, 12, 5)
previous_scores = st.slider("Previous Scores", 0, 100, 50)
extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])
sleep_hours = st.slider("Sleep Hours", 0, 12, 6)
papers_practiced = st.slider("Sample Papers Practiced", 0, 10, 3)

extracurricular = 1 if extracurricular == "Yes" else 0

if st.button("Predict"):
    input_data = np.array([[hours_studied, previous_scores, extracurricular, sleep_hours, papers_practiced]])
    prediction = model.predict(input_data)

    score = prediction[0]

    st.success(f"Predicted Performance Index: {score:.2f}")

    if score > 80:
        st.write("🔥 Excellent Performance")
    elif score > 60:
        st.write("👍 Good Performance")
    else:
        st.write("⚠️ Needs Improvement")