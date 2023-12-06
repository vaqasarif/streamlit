import streamlit as st
import joblib
import numpy as np
import requests
from io import BytesIO

# Load the trained model

# Define the URL to the raw joblib file on GitHub
model_url = "https://raw.githubusercontent.com/vaqasarif/streamlit/main/response.joblib"

# Download the model file from GitHub
response = requests.get(model_url)
model_bytes = BytesIO(response.content)

# Load the model
model = joblib.load(model_bytes)

# Title of the web app
st.title('Machine Learning Model Deployment')

# Create input fields for the form
input_fields = []
for i in range(10):
    input_fields.append(st.text_input(f'Input {i+1}', value=''))

# Convert input data to a numpy array
input_data = np.array([str(field) for field in input_fields])

# Make a prediction when a button is clicked
if st.button('Predict'):
    # Reshape the input data to match the model's expected input shape
    input_data = input_data.reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f'The predicted output is: {prediction[0]}')
