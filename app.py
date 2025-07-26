import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Mapping class IDs to crop names
crop_dict = {
    1: "🌾 Rice", 2: "🌽 Maize", 3: "🧵 Jute", 4: "👕 Cotton", 5: "🥥 Coconut", 6: "🍈 Papaya", 7: "🍊 Orange",
    8: "🍎 Apple", 9: "🍈 Muskmelon", 10: "🍉 Watermelon", 11: "🍇 Grapes", 12: "🥭 Mango", 13: "🍌 Banana",
    14: "🍎 Pomegranate", 15: "🥣 Lentil", 16: "🖤 Blackgram", 17: "🟢 Mungbean", 18: "🌱 Mothbeans",
    19: "🟡 Pigeonpeas", 20: "🍛 Kidneybeans", 21: "🥙 Chickpea", 22: "☕ Coffee"
}

# --- UI Layout ---
st.set_page_config(page_title="Crop Recommendation", page_icon="🌿", layout="centered")
st.title("🌿 Smart Crop Recommendation System")
st.markdown("Predict the **best crop** to cultivate based on soil and environmental conditions.")

# --- Input Form ---
with st.form("crop_form"):
    col1, col2 = st.columns(2)

    with col1:
        N = st.number_input("🧪 Nitrogen (N)", min_value=0, step=1)
        P = st.number_input("🧪 Phosphorus (P)", min_value=0, step=1)
        K = st.number_input("🧪 Potassium (K)", min_value=0, step=1)
        ph = st.number_input("🌡️ Soil pH", min_value=0.0, max_value=14.0, format="%.2f")

    with col2:
        temp = st.number_input("🌤️ Temperature (°C)", format="%.2f")
        humidity = st.number_input("💧 Humidity (%)", min_value=0, max_value=100)
        rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0)

    submitted = st.form_submit_button("🚀 Predict Crop")

# --- Prediction & Output ---
if submitted:
    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(features)

    crop = crop_dict.get(prediction[0], None)
    st.markdown("---")

    if crop:
        st.success(f"✅ **Recommended Crop**: {crop}")
        st.balloons()
    else:
        st.error("❌ Unable to determine a suitable crop. Please check your inputs.")

# --- Footer ---
st.markdown("---")
st.info("📌 This model is based on soil nutrients, temperature, humidity, pH, and rainfall conditions.\n\nDeveloped using `scikit-learn` & `Streamlit`.")




