import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("flight_delay_model.pkl", "rb"))

st.title("✈ Flight Delay Prediction System")

st.write("Enter flight details to predict whether a flight will be delayed.")

# User inputs
Month = st.slider("Month", 1, 12)
DayOfWeek = st.slider("Day of Week", 1, 7)

DepHour = st.slider("Departure Hour", 0, 23)
ArrHour = st.slider("Arrival Hour", 0, 23)

UniqueCarrier = st.number_input("Airline Code (encoded)", value=1)
Origin = st.number_input("Origin Airport (encoded)", value=1)
Dest = st.number_input("Destination Airport (encoded)", value=1)

Distance = st.number_input("Distance (miles)", value=500)

WeatherDelay = st.number_input("Weather Delay", value=0)
NASDelay = st.number_input("Air Traffic Delay", value=0)
LateAircraftDelay = st.number_input("Late Aircraft Delay", value=0)

# Create input dataframe
input_data = pd.DataFrame([[
    Month,
    DayOfWeek,
    DepHour,
    ArrHour,
    UniqueCarrier,
    Origin,
    Dest,
    Distance,
    WeatherDelay,
    NASDelay,
    LateAircraftDelay
]])

# Prediction
if st.button("Predict Delay"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠ Flight likely to be DELAYED")
    else:
        st.success("✅ Flight likely to be ON TIME")