import streamlit as st
import numpy as np
import joblib  # or import your model loading method

# Load your trained model
model = joblib.load("crop_recommendation_model.pkl")  # change the path if needed

# Crop label mapping (you can modify as per your model's classes)
crop_dict = {
    0: "Rice",
    1: "Wheat",
    2: "Maize",
    3: "Cotton",
    4: "Sugarcane",
    5: "Barley",
    6: "Groundnut",
    7: "Millet",
    8: "Pulses",
    9: "Tobacco",
    # Add more if needed...
}

# Streamlit App
st.set_page_config(page_title="Crop Recommendation System", layout="centered")

st.markdown("🌱 # Crop Recommendation System")
st.markdown("### Enter the soil and weather conditions:")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    N = st.text_input("Nitrogen", placeholder="e.g. 90")
with col2:
    P = st.text_input("Phosphorus", placeholder="e.g. 40")
with col3:
    K = st.text_input("Potassium", placeholder="e.g. 60")

col4, col5, col6 = st.columns(3)
with col4:
    temp = st.text_input("Temperature (°C)", placeholder="e.g. 25.5")
with col5:
    humidity = st.text_input("Humidity (%)", placeholder="e.g. 80")
with col6:
    ph = st.text_input("pH", placeholder="e.g. 6.5")

rainfall = st.text_input("Rainfall (mm)", placeholder="e.g. 100")

if st.button("Get Recommendation"):
    try:
        # Convert inputs to appropriate types
        features = np.array([[
            int(N), int(P), int(K),
            float(temp), float(humidity),
            float(ph), float(rainfall)
        ]])
        
        # Predict crop
        prediction = model.predict(features)
        crop = crop_dict.get(prediction[0], "Unknown Crop")
        
        st.markdown("---")
        st.success(f"✅ **Recommended Crop:** {crop}")
    
    except ValueError:
        st.error("🚫 Please enter valid numeric values in all fields.")
