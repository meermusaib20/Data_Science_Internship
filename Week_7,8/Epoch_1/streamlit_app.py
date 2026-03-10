import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("campaign_response_model.pkl","rb"))

st.title("Campaign Response Predictor")

income = st.number_input("Income")
recency = st.number_input("Recency")
age = st.number_input("Age")
spending = st.number_input("Total Spending")

features = np.array([[income, recency, age, spending]])

if st.button("Predict"):
    prediction = model.predict(features)
    st.write("Response:", "Yes" if prediction[0]==1 else "No")