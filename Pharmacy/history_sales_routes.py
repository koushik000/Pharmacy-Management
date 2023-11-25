import streamlit as st
from db_connector import get_connection

def get_history_sales():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Select relevant columns from history_sales and drugs tables
            cursor.execute("""
                SELECT hs.*, d.name as drug_name
                FROM history_sales hs
                JOIN drugs d ON hs.drug_id = d.id;
            """)
            # Fetch column names from cursor.description
            column_names = [column[0] for column in cursor.description]
            # Fetch all rows including column names
            result = [dict(zip(column_names, row)) for row in cursor.fetchall()]
    finally:
        connection.close()
    return result




def edit_history_sale(history_sale_id, new_amount):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Update the amount for the specified history sale ID
            cursor.execute("UPDATE history_sales SET total_amount = %s WHERE id = %s;", (new_amount, history_sale_id))
        connection.commit()
    finally:
        connection.close()

def delete_history_sale(history_sale_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Delete the history sale record for the specified ID
            cursor.execute("DELETE FROM history_sales WHERE id = %s;", (history_sale_id,))
        connection.commit()
    finally:
        connection.close()

def history_sales_page():
    st.title("History Sales")

    # Fetch history sales records
    history_sales = get_history_sales()

    # Display history sales records in a DataFrame
    st.dataframe(history_sales)

    # Add "Edit" and "Delete" options
    selected_sale_id = st.text_input("Enter the ID of the sale you want to edit or delete:")
    new_amount = st.text_input("Enter the new amount for editing:")

    if st.button("Edit"):
        if selected_sale_id and new_amount:
            edit_history_sale(int(selected_sale_id), float(new_amount))
            st.success("Sale edited successfully!")
        else:
            st.warning("Please enter both the sale ID and the new amount.")

    if st.button("Delete"):
        if selected_sale_id:
            delete_history_sale(int(selected_sale_id))
            st.success("Sale deleted successfully!")
        else:
            st.warning("Please enter the sale ID.")