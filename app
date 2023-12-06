# app.py
import streamlit as st

def main():
    # Title of the web app
    st.title('Form with 10 Input Fields')

    # Create a form with 10 input fields
    with st.form('Input Form'):
        # Create 10 input fields
        input_fields = []
        for i in range(10):
            input_fields.append(st.text_input(f'Input {i+1}', key=f'input_{i+1}', value=''))

        # Add a submit button to the form
        submitted = st.form_submit_button('Submit')

        # When the form is submitted
        if submitted:
            # Display the input data
            for i, value in enumerate(input_fields):
                st.write(f'Input {i+1}: {value}')

if __name__ == '__main__':
    main()
