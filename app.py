
import streamlit as st
import pandas as pd
import google.generativeai as genai

# Title
st.title("💡 Tech Mentor Chatbot (Powered by Gemini)")

# Load your dataset
data = pd.read_csv("tech_mentor_dataset.csv")

# Configure Gemini
genai.configure(api_key="AIzaSyBSnVks5STjwbW9GSGs9a9-ivpM4VMM9Po")  

model = genai.GenerativeModel("gemini-2.0-flash")

# Chat input
user_input = st.text_input("Ask me anything related to tech mentorship 👇")

if user_input:
    # You can enhance this by referencing your dataset
    context = data
    prompt = f"Using the following dataset context:\n{context}\nUser question: {user_input}"

    response = model.generate_content(prompt)
    st.write("**Bot:**", response.text)

