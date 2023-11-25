# invoice_routes.py
import streamlit as st
from db_connector import get_connection

def invoice_page():
    st.subheader("Invoice Page")

    # Fetch drugs for dropdown
    drugs = fetch_drugs()

    # Collect invoice details
    drug_name = st.selectbox("Select Drug", drugs)
    quantity = st.number_input("Quantity", min_value=1, value=1)
    price = st.number_input("Price", min_value=0.01, value=0.01)

    if st.button("Add to Invoice"):
        # Retrieve drug_id for the selected drug name
        drug_id = get_drug_id(drug_name)

        # Save the invoice details to the database
        save_invoice(drug_id, quantity, price)

        st.success("Item added to invoice successfully!")

def fetch_drugs():
    connection = get_connection()
    cursor = connection.cursor()

    # Fetch drug names from the drugs table
    cursor.execute("SELECT name FROM drugs")
    drugs = [row[0] for row in cursor.fetchall()]

    connection.close()
    return drugs

def get_drug_id(drug_name):
    connection = get_connection()
    cursor = connection.cursor()

    # Retrieve the drug_id for the selected drug name
    cursor.execute("SELECT id FROM drugs WHERE name=%s", (drug_name,))
    drug_id = cursor.fetchone()[0]

    connection.close()
    return drug_id

def save_invoice(drug_id, quantity, price):
    connection = get_connection()
    cursor = connection.cursor()

    # Save the invoice details to the database
    cursor.execute("INSERT INTO invoice (drug_id, quantity, price) VALUES (%s, %s, %s)", (drug_id, quantity, price))
    connection.commit()

    connection.close()
