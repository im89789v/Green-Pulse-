# 🌱 GreenPulse AI – Smart Precision Irrigation Advisor

### Green Planet | GP-02 | AI-Based Precision Irrigation Advisory

## 💡 About the Project

GreenPulse AI is a Python-based Machine Learning project designed to support sustainable agriculture through intelligent irrigation recommendations.

The application analyses soil and environmental conditions to estimate the amount of water required for crops.

Our goal is to reduce unnecessary water usage and encourage smarter irrigation practices.

## 🎯 Problem Statement

Traditional irrigation methods often depend on fixed schedules or manual judgement.

This can result in unnecessary water usage and inefficient irrigation.

GreenPulse AI aims to address this problem using Machine Learning.

## 🚀 Key Features

- 🌱 Crop-based irrigation estimation
- 💧 Soil moisture analysis using user inputs
- 🌡️ Temperature and humidity consideration
- 🌧️ Expected rainfall consideration
- 🤖 Machine Learning-based prediction
- 📊 Interactive dashboard
- 🌍 Sustainable water management

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Dataset handling |
| NumPy | Numerical calculations |
| Scikit-learn | Machine Learning |
| Random Forest | Prediction algorithm |
| Streamlit | Web application |
| Joblib | Model saving and loading |

## 🧠 Machine Learning Approach

We use a Random Forest Regression algorithm.

### Input Features

- Soil moisture
- Temperature
- Humidity
- Expected rainfall
- Crop type
- Soil type
- Crop growth stage

### Output

The model estimates the irrigation water requirement in millimetres.

The application also converts this estimate into litres based on the entered farm area.

## 📂 Project Structure

GreenPulse-AI/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── irrigation_data.csv
│
└── models/
    └── irrigation_model.pkl

## ⚙️ Installation and Setup

### Step 1: Clone the repository

git clone https://github.com/YOUR-USERNAME/GreenPulse-AI.git

### Step 2: Open the project folder

cd GreenPulse-AI

### Step 3: Install dependencies

pip install -r requirements.txt

### Step 4: Train the Machine Learning model

python train_model.py

### Step 5: Run the application

streamlit run app.py

## 📊 How It Works

1. User enters crop information.
2. User provides soil and environmental conditions.
3. Input data is processed by the application.
4. Random Forest predicts irrigation demand.
5. The dashboard displays the estimated water requirement.

## 🌍 Social Impact

GreenPulse AI aims to:

- Encourage efficient water usage.
- Support sustainable agriculture.
- Reduce unnecessary irrigation.
- Promote technology-driven farming.

## ⚠️ Dataset Disclaimer

The current prototype uses a synthetically generated demonstration dataset.

The model has not been trained or validated using actual agricultural field measurements. Its predictions are for demonstration purposes and should not be used as real-world irrigation instructions without expert validation.

## 🔮 Future Improvements

- Integration with real soil moisture sensors.
- Live weather API integration.
- Satellite-based agricultural data.
- Crop-specific recommendations using validated datasets.
- Mobile application for farmers.

## 👥 Project Information

**Project Name:** GreenPulse AI

**Theme:** Green Planet

**Problem ID:** GP-02

**Domain:** Artificial Intelligence and Machine Learning

**Programming Language:** Python

---

### 🌱 GreenPulse AI
**Smart Technology for a Greener Planet.**