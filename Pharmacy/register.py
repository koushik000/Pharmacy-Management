# register.py
import streamlit as st
from db_connector import get_connection

def registration_page():
    st.subheader("Register")

    # Add registration-related functionality here using st components
    new_username = st.text_input("New Username:")
    new_password = st.text_input("New Password:", type="password")

    if st.button("Register"):
        # You can use the database connection from db_connector.py
        connection = get_connection()

        # Perform user registration here (sample code)
        cursor = connection.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM login WHERE username=%s", (new_username,))
        result = cursor.fetchone()

        if result:
            st.error("Username already exists. Choose a different username.")
        else:
            # If the username doesn't exist, insert the new user
            cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)",
                           (new_username, new_password))
            connection.commit()

            st.success("Registration successful! You can now login.")

            # Close the connection when done
            connection.close()
            return True

    return False
