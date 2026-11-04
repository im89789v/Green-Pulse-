from pathlib import Path
import subprocess
import sys

import joblib
import pandas as pd
import streamlit as st

# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "irrigation_model.pkl"

# Page configuration
st.set_page_config(
    page_title="GreenPulse AI",
    page_icon="🌱",
    layout="centered"
)

# Load trained ML model
@st.cache_resource
def load_model():

    # Train model automatically if it doesn't exist
    if not MODEL_PATH.exists():
        subprocess.run(
            [sys.executable, str(BASE_DIR / "train_model.py")],
            check=True,
            cwd=BASE_DIR
        )

    return joblib.load(MODEL_PATH)


# Application heading
st.title("🌱 GreenPulse AI")
st.subheader("AI-Based Precision Irrigation Advisor")

st.write(
    "Smart irrigation recommendations using "
    "Machine Learning."
)

st.info(
    "This is a software prototype. "
    "Enter your field conditions manually. "
    "No physical sensors are required."
)

# Farmer inputs
st.header("🌾 Farm Information")

crop = st.selectbox(
    "Select your crop",
    ["Rice", "Tomato", "Wheat", "Maize", "Cotton"]
)

soil_type = st.selectbox(
    "Select soil type",
    ["Sandy", "Loamy", "Clay"]
)

growth_stage = st.selectbox(
    "Crop growth stage",
    ["Early", "Vegetative", "Flowering", "Maturity"]
)

st.header("🌤️ Environmental Conditions")

soil_moisture = st.slider(
    "Soil Moisture (%)", 5, 65, 25
)

temperature = st.slider(
    "Temperature (°C)", 15, 43, 30
)

humidity = st.slider(
    "Humidity (%)", 20, 95, 55
)

rainfall = st.slider(
    "Expected Rainfall (mm)", 0.0, 25.0, 2.0
)

farm_area = st.number_input(
    "Farm Area (square metres)",
    min_value=1.0,
    value=100.0,
    step=10.0
)

# Prediction button
if st.button("🌱 Generate Irrigation Advice"):

    try:
        model = load_model()

        # Prepare input for ML model
        input_data = pd.DataFrame([{
            "soil_moisture": soil_moisture,
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall,
            "crop": crop,
            "soil_type": soil_type,
            "growth_stage": growth_stage
        }])

        # Machine Learning prediction
        prediction = float(model.predict(input_data)[0])

        # Keep output within demo model range
        prediction = max(0.0, min(12.0, prediction))

        # Water calculation
        water_per_sqm = prediction
        total_water = water_per_sqm * farm_area

        # Display results
        st.divider()
        st.header("💧 Irrigation Recommendation")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Water Depth",
            f"{prediction:.2f} mm"
        )

        col2.metric(
            "Water per m²",
            f"{water_per_sqm:.2f} L"
        )

        col3.metric(
            "Total Water",
            f"{total_water:,.0f} L"
        )

        # Advisory message
        if prediction < 1:
            st.success(
                "Low irrigation requirement. "
                "Check soil moisture again before watering."
            )

        elif prediction < 4:
            st.info(
                "Moderate irrigation requirement. "
                "Check field conditions before watering."
            )

        else:
            st.warning(
                "Higher irrigation requirement estimated. "
                "Verify field conditions before applying water."
            )

        # Input summary
        st.subheader("📊 Field Analysis")

        st.write(f"**Crop:** {crop}")
        st.write(f"**Soil Type:** {soil_type}")
        st.write(f"**Growth Stage:** {growth_stage}")
        st.write(f"**Soil Moisture:** {soil_moisture}%")
        st.write(f"**Temperature:** {temperature}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Expected Rainfall:** {rainfall} mm")

        st.caption(
            "Prototype estimate based on synthetic training data. "
            "Not validated agricultural advice. Verify with field "
            "measurements and an agricultural expert."
        )

    except Exception as error:
        st.error(f"Prediction error: {error}")


# Footer
st.divider()

st.caption(
    "GreenPulse AI | Green Planet GP-02 | "
    "AI for Sustainable Agriculture 🌍"
)