import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('your_model.joblib')

# Title of the web app
st.title('Machine Learning Model Deployment')

# Create input fields for the form
input_fields = []
for i in range(10):
    input_fields.append(st.text_input(f'Input {i+1}', value=''))

# Convert input data to a numpy array
input_data = np.array([float(field) for field in input_fields])

# Make a prediction when a button is clicked
if st.button('Predict'):
    # Reshape the input data to match the model's expected input shape
    input_data = input_data.reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f'The predicted output is: {prediction[0]}')
