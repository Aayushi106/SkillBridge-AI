import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBkOBuzh8CU934rdcG8IQdW6FpLFUHvpRI")

model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("SkillBridge AI 🚀")
st.subheader("Personalized Career Roadmap Generator")

career_goal = st.text_input("What career are you targeting?")
current_skills = st.text_area("List your current skills")
experience_level = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
weekly_hours = st.number_input("How many hours per week can you study?", min_value=1, max_value=60)

if st.button("Generate Roadmap"):

    prompt = f"""
    You are an expert career mentor.

    Create a structured roadmap.

    Career Goal: {career_goal}
    Current Skills: {current_skills}
    Experience Level: {experience_level}
    Weekly Study Hours: {weekly_hours}

    Format with:
    1. Skill Gap Analysis
    2. Priority Learning Path
    3. 12-Week Plan
    4. Projects
    5. Resources
    """

    response = model.generate_content(prompt)

    st.markdown(response.text)
