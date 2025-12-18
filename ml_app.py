import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Load the trained model
joblib_file = "heart_disease_model.pkl"
model = joblib.load(joblib_file)

# Streamlit app title
st.title("Heart Disease Prediction App")

# Input features from the user
st.sidebar.header("Input Features")

age = st.sidebar.slider("Age", 20, 100, 50)
gender = st.sidebar.selectbox("Gender", ["male", "female"])
bmi = st.sidebar.slider("BMI", 10, 50, 25)
blood_pressure = st.sidebar.selectbox("Blood Pressure", ["normal", "high", "low"])
fbs = st.sidebar.slider("Fasting Blood Sugar (mg/dL)", 50, 200, 100)
hba1c = st.sidebar.slider("HbA1c (%)", 3.0, 10.0, 5.5)
family_history = st.sidebar.selectbox("Family History of Diabetes", ["no", "yes"])
smoking = st.sidebar.selectbox("Smoking", ["no", "yes"])
diet = st.sidebar.selectbox("Diet", ["healthy", "poor"])
exercise = st.sidebar.selectbox("Exercise", ["regular", "no"])

# Convert input features to dataframe
input_features = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'blood_pressure': [blood_pressure],
    'fbs': [fbs],
    'hba1c': [hba1c],
    'family_history_of_diabetes': [family_history],
    'smoking': [smoking],
    'diet': [diet],
    'exercise': [exercise],
    'gender_male': [gender]
})

encoding_map={
    'family_history_of_diabetes':{"no":0,"yes":1},
    'smoking':{"yes":1,"no":0},
    'diet':{"poor":1,"healthy":1},
    'exercise':{"no":0,'regular':1},
    'blood_pressure':{'high':2,'normal':1,'low':0},
    'gender_male':{'male':1,'female':0}
    }

for col in encoding_map:
    input_features[col]=input_features[col].replace(encoding_map[col])
print(input_features)
# Prediction
prediction = model.predict(input_features.values)
prediction_proba = model.predict_proba(input_features)
print(prediction)
# Display the prediction
st.subheader("Prediction")
st.write(f"Predicted Diagnosis: {prediction[0]}")


# Display additional information
st.subheader("Class Labels")
st.write(["No", "Yes"])
