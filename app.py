import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('random_forest_model.pkl')

st.title("Credit Card Fraud Detection App")

st.markdown("""
Enter transaction details below. All features must be filled in as per your model's requirements.
""")

# Example input fields for features (add all features used by your model)
# For demonstration, we'll use just 'Time' and 'Amount' and 28 PCA features (V1-V28).
# You need to add all features for your model to work correctly.

time = st.number_input("Time", value=0.0)
amount = st.number_input("Amount", value=0.0)
v_inputs = []
for i in range(1, 29):
    v = st.number_input(f"V{i}", value=0.0)
    v_inputs.append(v)

# When the user clicks 'Predict'
if st.button("Check for Fraud"):
    # Arrange inputs in the same order as your model expects
    features = [time] + v_inputs + [amount]
    input_array = np.array([features])
    prediction = model.predict(input_array)
    if prediction[0] == 1:
        st.error("Fraudulent Transaction Detected!")
    else:
        st.success("Transaction is Legitimate.")
