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
**Main Website*: <img width="1782" height="915" alt="Screenshot 2025-07-26 214139" src="https://github.com/user-attachments/assets/2e07135f-fffb-4ecd-9a74-91ab3bd657de" />

🌿 **Crop Recommendation App**: <img width="1289" height="893" alt="Screenshot 2025-07-26 214250" src="https://github.com/user-attachments/assets/ba6f205f-896f-4659-96f7-d4cb1e6e5fc0" />



📜 License
This project is licensed under the MIT License.


