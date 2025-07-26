# 🌱 SeedSpring

Welcome to **SeedSpring** — your intelligent farming assistant!  
This project leverages machine learning to provide **crop recommendations** based on soil and weather conditions, helping farmers and agricultural enthusiasts make data-driven decisions.

---

## 🔗 Live Project Links

- 🌐 **Main Website**: [SeedSpring Website](https://anishka24.github.io/SeedSpring/)
- 🌿 **Crop Recommendation App**: [Launch Predictor](https://seedspring-g6x5tleyrjhpcr43urpwnc.streamlit.app/)

---

## 🤖 Crop Recommendation System

The Crop Recommendation System predicts the **most suitable crop** to grow based on the following input parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

### 🧠 Model
A machine learning classification model (e.g., RandomForest) trained on a dataset of soil and climate features mapped to ideal crops. The trained model is serialized using `pickle`.

### 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python, scikit-learn, NumPy
- **Deployment**: Streamlit Cloud + GitHub Pages

---

## 📁 Project Structure

```bash
SeedSpring/
├── app.py                # Streamlit-based crop recommendation app
├── model.pkl             # Trained ML model file
├── requirements.txt      # Python dependencies
├── website/              # GitHub Pages frontend (HTML/CSS/JS)
└── README.md             # This file
🚀 How to Run Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/anishka24/SeedSpring.git
cd SeedSpring
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
🙋‍♀️ Author
Anishka Singh
🔗 GitHub

📜 License
This project is licensed under the MIT License.

yaml
Copy
Edit
