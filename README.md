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

## Steps to run locally

Clone the repository or download the zip file.
Extract all the files.
Deploy the index.html file on github or run it locally through your browser.
Deployment of crop recommendation is done through streamlit.

🙋‍♀️ Author
Anishka Singh
🔗 GitHub

Preview 

<img width="1782" height="912" alt="image" src="https://github.com/user-attachments/assets/6fece4aa-2c43-447a-b1e5-d578f82d7f07" />





