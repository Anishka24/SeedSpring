# import streamlit as st
# import pickle
# import numpy as np

# # Load model
# model = pickle.load(open("model.pkl", "rb"))

# # Crop dictionary
# crop_dict = {
#     1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
#     8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
#     14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
#     19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
# }

# # CSS styling
# st.markdown("""
#     <style>
#     .main {
#         max-width: 750px;
#         margin: auto;
#         padding: 2rem;
#         background: #f5fff1;
#         border-radius: 10px;
#         box-shadow: 0 0 15px rgba(0,0,0,0.05);
#     }
#     .stButton {
#         display: flex;
#         justify-content: center;
#         margin-top: 2rem;
#     }
#     .stButton>button {
#         background-color: #4caf50;
#         color: white;
#         padding: 10px 24px;
#         border-radius: 8px;
#         font-size: 16px;
#         border: none;
#     }
#     .stButton>button:hover {
#         background-color: #388e3c;
#     }
#     .title {
#         text-align: center;
#         font-size: 2.5rem;
#         color: #2e7d32;
#         font-weight: bold;
#     }
#     .result {
#         font-size: 1.5rem;
#         padding: 1rem;
#         border-radius: 8px;
#         background: #e8f5e9;
#         color: #1b5e20;
#         text-align: center;
#         margin-top: 2rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown('<div class="main">', unsafe_allow_html=True)
# st.markdown('<div class="title">🌱 Crop Recommendation System</div>', unsafe_allow_html=True)
# st.write("### Enter soil and climate conditions:")

# # Inputs
# N = st.number_input("Nitrogen (e.g. 90)", value=0)
# P = st.number_input("Phosphorus (e.g. 40)", value=0)
# K = st.number_input("Potassium (e.g. 60)", value=0)
# temp = st.number_input("Temperature (°C)", format="%.2f")
# humidity = st.number_input("Humidity (%)", format="%.2f")
# ph = st.number_input("pH", format="%.2f")
# rainfall = st.number_input("Rainfall (mm)", format="%.2f")

# # Predict Button
# centered_button = st.container()
# with centered_button:
#     submit = st.button("Predict")

# # Prediction
# if submit:
#     features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
#     prediction = model.predict(features)
#     crop_name = crop_dict.get(prediction[0], prediction[0])

   
#     st.markdown(f"""
#         <div class="result">
#             <strong>Recommended Crop for Cultivation:</strong><br>
#             {crop_name} is the best crop to be cultivated right there.
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)
from flask import Flask, request, render_template
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("crop_recommendation.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        N = int(request.form['Nitrogen'])
        P = int(request.form['Phosporus'])
        K = int(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])

        features = np.array([N, P, K, temp, humidity, ph, rainfall]).reshape(1, -1)
        prediction = model.predict(features)
        crop = prediction[0]  # Assuming the model outputs string labels
        result = f"{crop} is the best crop to be cultivated right there"

    except Exception as e:
        result = f"Error in input or prediction: {str(e)}"

    return render_template('crop_recommendation.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

