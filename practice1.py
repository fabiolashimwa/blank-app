import streamlit as st
from PIL import Image
import pytesseract
import datetime

st.title("Salary predictor 🔮")
# This line of code displays Salary predictor in a title format
st.write("Hi, welcome...do you want to know your estimated monthly salary? Let's start😊🤗")
# This line of code write arguments to our app
input_mode = st.radio("How would you like to provide your personal details?", ["Type manually", "Scan ID using camera"])
first_name = st.text_input("First Name")
last_name = st.text_input("Last name")
# These two lines allow the user to input his/her information
gender = st.selectbox("Gender", ["Male", "Female"])
# This line displays a box with gender option to choose
age = st.number_input("Your age", 15, 80, 30, 1)
# This line allows the user to input his age. The minimum age is 15 and max_age is 80. The default age is 30 and the difference between ages is 1
date_of_birth = st.date_input("your bithday")
if input_mode == "Type manually":
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    date_of_birth = st.date_input("Date of Birth")

# --- Option 2: Camera Input ---
elif input_mode == "Scan ID using camera":
    image = st.camera_input("📸 Scan your ID")

    if image:
        image_data = Image.open(image)
        extracted_text = pytesseract.image_to_string(image_data)

        st.text_area("📝 Extracted Text (for review)", extracted_text, height=150)

        # Example: very simple parsing
        lines = extracted_text.split('\n')
        
        for line in lines:
            if "First" in line:
                first_name = line.split(":")[-1].strip()
            elif "Last" in line:
                last_name = line.split(":")[-1].strip()
            elif "DOB" in line or "Birth" in line:
                date_str = line.split(":")[-1].strip()
                try:
                    date_of_birth = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                except:
                    date_of_birth = ""

        # Show extracted or fallback input
        st.text_input("First Name", value=first_name)
        st.text_input("Last Name", value=last_name)
        if date_of_birth:
            st.date_input("Date of Birth")
        else:
            st.warning("Couldn't detect birth date. Please enter it manually.")
            date_of_birth = st.date_input("Date of Birth")

# You can now use first_name, last_name, date_of_birth in the rest of your form

# This line allows the user to input his/her date of birth
marital_status = st.pills("Marital status", ["Single", "Married" ,"Divorced"])
# This line allows a single select option
years_of_experience = st.slider("Years of experience", 0, 40)
# This display a slider to select the years of experience in the range 0-40
years_of_study = st.number_input("Years of study",6, 40)
# This line allows the user to input the years of study 
level_of_studies = st.selectbox("Level of studies", ["High school degree", "Bachelor degree", "Master degree", "PHD degree"])
number_of_certification = st.selectbox("Nummber of certicates", ["1","2", "3", "4", "5" ,"+5"])
work_domain = st.selectbox("Work domain", ["Information technology/Computing", "Healthcare/Medicine/Nursing", "Education/Teaching", "Engineering/Industry/Constuction", "Finance/Baking/Insurance", "Sales/Marketing/Commerce", "Administration/Management/Human Ressources", "Arts/Culture/Media/Communication", "Transportation/Logistics", "Hospitality/Food service/Tourism", "Agriculture/Agri-food", "Law/Legal service", "Research/Sciences", "Social service/social work", "Public administration/Government", "International trade/Export-Import", "Energy/Environment", "Sport/Recreation/Entertainment", "Real Estate", "Craftsmanship/Manufacturing/Maintenance", "Telecommunication", "Multimedia/Design/Graphic arts", "Pharmaceutical/Biotechnology", "Security/Defense/Police", "Fashion/Textile/Luxury Goods"])
job_levels = st.selectbox("Job level", ["Intern", "Assistant", "Junior", "Intermediate/Analyst/Specialist", "Senior"])
work_sectors = st.selectbox("Work sector", ["Public/Government sector", "NGOs/Internation Organizations", "Private companies", "Research Institutes/Universities", "Health sector","Techonology sector", "Industrial sector", "Freelance/Independent", "Informal/Community sector"])
# These three lines allow a single select option
#Generate the output
if st.button("Generate the output"):
# This line displays a button 
    monthly_estimated_salary = ...# calculate the salary in american dollars using a given formula
    # convert the salary in another currence
    st.write(f"The monthly salary is estimated to: {monthly_estimated_salary} USD")
else:
    st.write("Press the button to generate the result")    
st.feedback('faces')
# This line displays a rating button