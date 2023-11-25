# sales_routes.py
import streamlit as st
from db_connector import get_connection

def sales_page():
    st.subheader("Sales Page")

    # Fetch drugs for dropdown
    drugs = fetch_drugs()

    # Collect sales details
    drug_name = st.selectbox("Select Drug", drugs)
    quantity = st.number_input("Quantity Sold", min_value=1, value=1)
    total_amount = st.number_input("Total Amount", min_value=0.01, value=0.01)

    if st.button("Record Sale"):
        # Save the sales details to the database
        save_sale(drug_name, quantity, total_amount)

        st.success("Sale recorded successfully!")

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

def save_sale(drug_name, quantity, total_amount):
    connection = get_connection()
    cursor = connection.cursor()

    drug_id = get_drug_id(drug_name)

    # Save the sale details to the sales table
    cursor.execute("INSERT INTO sales (drug_id, quantity, total_amount, sale_date) VALUES (%s, %s, %s, CURDATE())", (drug_id, quantity, total_amount))
    connection.commit()

    # Save the sale details to the history_sales table
    cursor.execute("INSERT INTO history_sales (drug_id, quantity_sold, total_amount, sale_date) VALUES (%s, %s, %s, CURDATE())", (drug_id, quantity, total_amount))
    connection.commit()

    connection.close()
