#Imports Streamlit, takes user input for height and weight, calculates BMI, displays result, provides BMI category with recommendations, and updates status based on BMI value.

import streamlit as st

st.title("BMI Calculator")

st.header("Enter Your Details")
height = st.slider("Enter your height {in cm}:", 100, 250, 175)
weight = st.slider("Enter your weight  {in kg}", 40, 200, 70)

bmi = weight / ((height/100) ** 2)

st.header("Your BMI Result")
st.write(f" **Your BMI is {bmi:.2f}** ")

st.header("BMI Ranges Explained")
st.write("- **Underweight:** BMI < 18.5")
st.write("- **Normal weight:** 18.5 - 24.9")
st.write("- **Overweight:** 25 - 29.9")
st.write("- **Obesity:** BMI ≥ 30")

st.header("Your BMI Status")
if bmi < 18.5:
    st.warning("🟡 **Underweight** (Consider a healthy diet to gain weight.)")
elif 18.5 <= bmi < 24.9:
    st.success("🟢 **Normal weight** (Great job! Maintain your healthy lifestyle.)")
elif 25 <= bmi < 29.9:
    st.info("🟠 **Overweight** (You may want to focus on diet and exercise.)")
else:
    st.error("🔴 **Obesity** (Consult a healthcare provider for a healthy weight plan.)")