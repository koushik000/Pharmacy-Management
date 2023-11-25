# drugs_routes.py
import streamlit as st
from db_connector import get_connection

def get_drugs():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, unit_price FROM drugs;")
            result = cursor.fetchall()
    finally:
        connection.close()
    return result
def drugs_page():
    st.title("Drugs Page")

    # Add drugs-related functionality here using st components
    name = st.text_input("Drug Name:")
    manufacturer = st.text_input("Manufacturer:")
    expiration_date = st.date_input("Expiration Date:")
    unit_price = st.number_input("Unit Price:")

    if st.button("Add Drug"):
        # You can use the database connection from db_connector.py
        connection = get_connection()

        # Perform database operations here (sample code)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO drugs (name, manufacturer, expiration_date, unit_price) VALUES (%s, %s, %s, %s)",
                       (name, manufacturer, expiration_date, unit_price))
        connection.commit()

        st.success("Drug added successfully!")

        # Close the connection when done
        connection.close()
