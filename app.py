import streamlit as st
import pandas as pd
import os
from openai import OpenAI

# --- CONFIGURATION ---
st.set_page_config(page_title="Abid-Hub: IT & Quran", layout="wide")
client = OpenAI(api_key="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") # Replace with your key later

# --- SIDEBAR: TRAINER SIGNUP ---
st.sidebar.header("Trainer Registration")
with st.sidebar.form("signup_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    subject = st.selectbox("Specialization", ["Online IT", "Online Quran"])
    email = st.text_input("Email")
    
    submitted = st.form_submit_button("Sign Up to Teach")
    if submitted:
        # Save to CSV (Our simple database)
        new_data = pd.DataFrame([[name, gender, subject, email]], 
                                columns=['Name', 'Gender', 'Subject', 'Email'])
        new_data.to_csv('trainers.csv', mode='a', header=not os.path.exists('trainers.csv'), index=False)
        st.sidebar.success(f"Welcome {name}! You are registered.")

# --- MAIN PAGE: AI CHAT ROOM ---
st.title("🤖 Abid-Hub AI Assistant")
st.info("Ask me anything about our IT Courses or Quran Teaching projects!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Custom Instructions for your dual-project
        system_instruction = "You are an assistant for Abid-Hub. Provide info on IT training and Quranic studies. Be professional and respectful."
        
        # Simple AI Response logic (Replace with API call)
        response = f"Thank you for asking about {prompt}. Our trainers (Male/Female) are ready to assist you!"
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})