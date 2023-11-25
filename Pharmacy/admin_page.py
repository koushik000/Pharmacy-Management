# admin_page.py
import streamlit as st
from authentication import authentication_page

def admin_page():
    st.title("Admin Page")

    # Display the authentication content
    authentication_page()
