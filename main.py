import streamlit as st

def calculate_map(systolic_pressure, diastolic_pressure):
    map = (2 * diastolic_pressure + systolic_pressure) / 3
    return map

# Streamlit app header
st.title("Mean Arterial Pressure (MAP) Calculator")

# User input for systolic and diastolic pressure
systolic = st.number_input("Enter systolic pressure (mmHg):", min_value=0.0, step=1.0)
diastolic = st.number_input("Enter diastolic pressure (mmHg):", min_value=0.0, step=1.0)

# Calculate MAP
map = calculate_map(systolic, diastolic)

# Display calculated MAP
st.subheader("Calculated MAP:")
st.write(f"{map:.2f} mmHg")
