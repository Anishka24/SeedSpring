import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open("model.pkl", "rb"))

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# CSS for centered layout and spacing
st.markdown("""
    <style>
        .main-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem 2rem 1rem 2rem;
            background-color: white;
            border-radius: 12px;
        }
        .stButton>button {
            background-color: #2d6a4f;
            color: white;
            padding: 10px 24px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #225c3e;
        }
        .title-style {
            text-align: center;
            color: #2d6a4f;
            font-weight: 700;
            font-size: 2.2rem;
        }
        .emoji {
            font-size: 2rem;
            margin-right: 10px;
            vertical-align: middle;
        }
    </style>
""", unsafe_allow_html=True)

# UI title
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="title-style"><span class="emoji">🌱</span>Crop Recommendation System</h1>', unsafe_allow_html=True)
st.write("### Enter the soil and weather conditions:")

# Form inputs
with st.form("crop_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        N = st.number_input("Nitrogen", min_value=0, placeholder="e.g. 90")
    with col2:
        P = st.number_input("Phosphorus", min_value=0, placeholder="e.g. 40")
    with col3:
        K = st.number_input("Potassium", min_value=0, placeholder="e.g. 60")

    col4, col5, col6 = st.columns(3)
    with col4:
        temp = st.number_input("Temperature (°C)", format="%.2f", placeholder="e.g. 25.5")
    with col5:
        humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, placeholder="e.g. 80")
    with col6:
        ph = st.number_input("pH", format="%.2f", placeholder="e.g. 6.5")

    rainfall = st.number_input("Rainfall (mm)", min_value=0, placeholder="e.g. 100")

    submitted = st.form_submit_button("Get Recommendation")

# Prediction logic
if submitted:
    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(features)
    crop = crop_dict.get(prediction[0], None)

    st.markdown("---")
    if crop:
        st.success(f"✅ **Recommended Crop:** {crop}")
    else:
        st.error("⚠️ Sorry, we could not determine a suitable crop.")

st.markdown("</div>", unsafe_allow_html=True)
