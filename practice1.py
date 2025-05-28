import streamlit as st
st.title("Title: Salary predictor")
st.write("Hi, welcome...do you want to know your estimated monthly salary? Let's start😊🤗")

first_name = st.text_input("First Name")
last_name = st.text_input("Last name")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Your age", 0, 100, 30, 1)
date_of_birth = st.date_input("your bithday")
marital_status = st.radio("Marital status", ["Single", "Married"])
years_of_experience = st.slider("Years of experience", 0, 40)
years_of_study = st.number_input("Years of study", 6, 20)
level_of_studies = st.selectbox("Level of studies", ["High school degree", "Bachelor degree", "Master degree", "PHD degree"])
number_of_certification = st.selectbox("Nummber of certicates", ["1","2", "3", "4", "5"])
work_domain = st.selectbox("Work domain", ["Information technology/Computing", "Healthcare/Medicine/Nursing", "Education/Teaching", "Engineering/Industry/Constuction", "Finance/Baking/Insurance", "Sales/Marketing/Commerce", "Administration/Management/Human Ressources", "Arts/Culture/Media/Communication", "Transportation/Logistics", "Hospitality/Food service/Tourism", "Agriculture/Agri-food", "Law/Legal service", "Research/Sciences", "Social service/social work", "Public administration/Government", "International trade/Export-Import", "Energy/Environment", "Sport/Recreation/Entertainment", "Real Estate", "Craftsmanship/Manufacturing/Maintenance", "Telecommunication", "Multimedia/Design/Graphic arts", "Pharmaceutical/Biotechnology", "Security/Defense/Police", "Fashion/Textile/Luxury Goods"])
#Generate the output
if st.button("Generate the output"):
    monthly_estimated_salary = ...# calculate the salary in american dollars using a given formula
    # convert the salary in another currence
    st.write(f"The monthly salary is estimated to: {monthly_estimated_salary} USD")
else:
    st.write("Press the button to generate the result")    