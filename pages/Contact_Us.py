import streamlit as st
from send_email import send_message

st.set_page_config(layout="wide")
st.title("Contact Me")

with st.form(key="user_form"):
    user_email = st.text_input("Your email address", placeholder="Write your email")
    raw_message = st.text_area("Your message", placeholder="Write your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_message(message)
        st.success("Your email was sent successfully!")
