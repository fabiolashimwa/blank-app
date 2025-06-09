import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("salaryData.csv")
st.title("Salary predictor 🔮")
# This line of code displays Salary predictor in a title format
st.write("Hi, welcome...do you want to know your estimated monthly salary? Let's start😊🤗")
# This line of code write arguments to our app

first_name = st.text_input("First Name")
last_name = st.text_input("Last name")
# These two lines allow the user to input his/her information
gender = st.selectbox("Gender", ["Male", "Female"])
# This line displays a box with gender option to choose
age = st.number_input("Your age", 23, 53, 30, 1)
# This line allows the user to input his age. The minimum age is 15 and max_age is 80. The default age is 30 and the difference between ages is 1
marital_status = st.pills("Marital status", ["Single", "Married" ,"Divorced"])
# This line allows a single select option
level_of_studies = st.selectbox("Level of studies", ["Bachelor", "Master", "PhD"])
years_of_experience = st.slider("Years of experience", 1, 29)
# This display a slider to select the years of experience in the range 1-29
job_titles = sorted(df["Job Title"].dropna().unique())
job_title = st.selectbox("Job title", job_titles)

model, model_columns = joblib.load('Salary predictor model.py')
inputs = pd.DataFrame([{"Age": age,"Gender": gender,"Education Level": level_of_studies,"Job Title": job_title,"Years of Experience": years_of_experience}])
data = pd.concat([inputs,df], axis=0)
data_converted = pd.get_dummies(data, columns=["Gender", "Education Level", "Job Title"], drop_first=True)
inputs_converted = data_converted.iloc[0:1]

for col in model_columns:
    if col not in inputs_converted:
       inputs_converted[col] = 0

inputs_converted = inputs_converted[model_columns]
    
if st.button("Generate the output"):
# This line displays a button 
    monthly_estimated_salary =model.predict(inputs_converted[0])
    st.write(f"The monthly salary is estimated to: **${monthly_estimated_salary}** USD")
st.feedback('faces')
# This line displays a rating button