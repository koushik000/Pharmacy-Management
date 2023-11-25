# login_routes.py
import streamlit as st
from db_connector import get_connection

def login_page():
    page_name = "login_page"  # Customize this based on your page structure

    st.subheader("Login")

    # Add login-related functionality here using st components
    username = st.text_input("Username", key=f"{page_name}_username_input")
    password = st.text_input("Password", type="password", key=f"{page_name}_password_input")

    if st.button("Login", key=f"{page_name}_login_button"):
        # You can use the database connection from db_connector.py
        connection = get_connection()

        # Perform login authentication here (sample code)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()

        if result:
            st.success("Login successful!")
            # Close the connection when done
            connection.close()
            return True
        else:
            st.error("Login failed. Invalid credentials.")

        # Close the connection when done
        connection.close()

    return False
