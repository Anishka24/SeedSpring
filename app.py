import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Streamlit UI
st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and weather conditions to get the best crop recommendation.")

# Input form
with st.form("crop_form"):
    N = st.number_input("Nitrogen", min_value=0)
    P = st.number_input("Phosphorus", min_value=0)
    K = st.number_input("Potassium", min_value=0)
    temp = st.number_input("Temperature (°C)", format="%.2f")
    humidity = st.number_input("Humidity (%)", min_value=0, max_value=100)
    ph = st.number_input("Soil pH", format="%.2f")
    rainfall = st.number_input("Rainfall (mm)", min_value=0)
    submitted = st.form_submit_button("Predict")

if submitted:
    # Prepare input
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    # Prediction
    prediction = model.predict(single_pred)

    # Output
    crop = crop_dict.get(prediction[0], None)
    if crop:
        st.success(f"✅ Recommended Crop: **{crop}**")
    else:
        st.error("⚠️ Sorry, we could not determine a suitable crop.")


