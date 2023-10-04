import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Load your machine learning model (replace with your model loading code)
loaded_model = pickle.load(open("rmtrained_model.sav", "rb"))
st.write("""
    <style>
        body {
            background-color: #f5f5f5; /* Change the background color */
            font-family: Arial, sans-serif; /* Change the font family */
        }

        h1 {
            color: #ffffff; /* Change the main heading color to white */
            font-size: 72px; /* Change the main heading font size */
            font-family: "Times New Roman", serif; /* Change the font for headings */
            transition: color 0.3s; /* Add a hover effect for color change */
           
            
        }

        h1:hover {
            color: #ff5733; /* Change the color on hover */
        }

        h2 {
            color: #ffffff; /* Change the subheading color to white */
            font-size: 100px; /* Change the subheading font size */
            font-family: "Times New Roman", serif; /* Change the font for headings */
            transition: color 0.3s; /* Add a hover effect for color change */
            margin-top: -60px;
            
        }

        h2:hover {
            color: #ff5733; /* Change the color on hover */
        }
        
        .stButton {
            display: flex;
            padding: 30px;
            justify-content: center;
        }
        
        image{
            width: 100px;
            display:center;
            justify-content:center;
        }

        .sidebar .stSlider .stSlider-content {
            background-color: #fff; /* Change the slider background color */
            border-radius: 8px; /* Add rounded corners to the slider */
        }

        /* Add more custom styles as needed */
    </style>
""", unsafe_allow_html=True)

def predict_coronary_disease(input_data):
    # Convert categorical inputs to numerical values
    input_data['fasting_blood_sugar'] = 1 if input_data['fasting_blood_sugar'] == 'Yes' else 0
    input_data['exercise_induced_angina'] = 1 if input_data['exercise_induced_angina'] == 'Yes' else 0

    # Convert the input data values to a NumPy array
    input_data_as_numpy_array = np.array(list(input_data.values())).reshape(1, -1)

    # Make predictions using the loaded model
    prediction = loaded_model.predict(input_data_as_numpy_array)

    return prediction


# Create the Streamlit web app
def main():
    st.image("heartimg.png", caption=None, width=55, use_column_width=None, clamp=False, channels="RGB",
            output_format="auto")

    st.title("Coronary Disease Prediction ")
   




    # Increase the font size of the subheading


    st.sidebar.header("User Input")

    # Define user input elements based on the new parameters
    age = st.sidebar.slider("Age", 0, 100, 50)
    resting_blood_pressure = st.sidebar.slider("Resting Blood Pressure", 90, 200, 120)
    cholesterol = st.sidebar.slider("Cholesterol", 100, 500, 200)
    fasting_blood_sugar = st.sidebar.radio("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    max_heart_rate_achieved = st.sidebar.slider("Max Heart Rate Achieved", 60, 220, 150)
    exercise_induced_angina = st.sidebar.radio("Exercise Induced Angina", ["No", "Yes"])
    st_depression = st.sidebar.slider("ST Depression", 0.0, 5.0, 2.0)
    sex_male = st.sidebar.radio("Sex (Male)", ["Female", "Male"])

    # Subheading for Chest Pain
    st.sidebar.subheader("Chest Pain")
    chest_pain_type_atypical = st.sidebar.checkbox("Atypical Angina")
    chest_pain_type_non_anginal = st.sidebar.checkbox("Non-Anginal Pain")
    chest_pain_type_typical = st.sidebar.checkbox("Typical Angina")

    # Add other parameters
    st.sidebar.subheader("Rest ECG")
    rest_ecg_left_hypertrophy = st.sidebar.checkbox("Left Ventricular Hypertrophy")
    rest_ecg_normal = st.sidebar.checkbox("Normal")

    st.sidebar.subheader("ST Slope")
    st_slope_flat = st.sidebar.checkbox("Flat")
    st_slope_upsloping = st.sidebar.checkbox("Upsloping")

    # Create a button to make predictions
    if st.sidebar.button("Predict"):
        # Prepare the user input as a dictionary
        input_data = {
            "age": age,
            "resting_blood_pressure": resting_blood_pressure,
            "cholesterol": cholesterol,
            "fasting_blood_sugar": fasting_blood_sugar,
            "max_heart_rate_achieved": max_heart_rate_achieved,
            "exercise_induced_angina": exercise_induced_angina,
            "st_depression": st_depression,
            "sex_male": 1 if sex_male == "Male" else 0,
            "chest_pain_type_atypical": 1 if chest_pain_type_atypical else 0,
            "chest_pain_type_non_anginal": 1 if chest_pain_type_non_anginal else 0,
            "chest_pain_type_typical": 1 if chest_pain_type_typical else 0,
            "rest_ecg_left_hypertrophy": 1 if rest_ecg_left_hypertrophy else 0,
            "rest_ecg_normal": 1 if rest_ecg_normal else 0,
            "st_slope_flat": 1 if st_slope_flat else 0,
            "st_slope_upsloping": 1 if st_slope_upsloping else 0
        }

        # Make a prediction
        prediction = predict_coronary_disease(input_data)

        # Display the prediction result
        if prediction[0] == 0:
            st.success("No Coronary Disease Detected")
        else:
            st.error("Coronary Disease Detected")

            # app.py

            # Add CSS styles to the app


if __name__ == "__main__":
    main()
