import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Crop Recommendation App")

# Inputs
N = st.number_input("Nitrogen", 0)
P = st.number_input("Phosphorus", 0)
K = st.number_input("Potassium", 0)
temp = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall")

if st.button("Predict"):
    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(features)
    st.success(f"Recommended crop: {prediction[0]}")
