# main.py
import streamlit as st
from admin_page import admin_page
from login_routes import login_page
from invoice_routes import invoice_page
from user_routes import users_page
from drug_routes import drugs_page
from sales_routes import sales_page
from history_sales_routes import history_sales_page  # Import the history_sales_page
from db_connector import get_connection

# Initialize session state
def init_session_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

# Function to run a database query
def run_database_query(query):
    # Replace these with your actual database connection details
    db_config = {
        'host': 'your_host',
        'user': 'your_user',
        'password': 'your_password',
        'database': 'your_database',
    }

    # Connect to the database
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            # Execute the query
            cursor.execute(query)
            # Fetch the result
            result = cursor.fetchall()
    finally:
        # Close the database connection
        connection.close()

    return result

# Main function
def main():
    init_session_state()
    st.title("Pharmacy Management")

    # Check if the user is authenticated
    authenticated = st.session_state.authenticated

    # If not authenticated, show the Admin page (authentication)
    if not authenticated:
        admin_page()

    # If authenticated, show the main content
    else:
        # Add a logout button to the left sidebar
        st.sidebar.button("Logout", on_click=logout)

        # Add navigation to different pages
        page = st.sidebar.selectbox("Select a page", ["Invoice", "Users", "Drugs", "Sales", "History Sales"])

        if page == "Invoice":
            invoice_page()
        elif page == "Users":
            users_page()
        elif page == "Drugs":
            drugs_page()
        elif page == "Sales":
            sales_page()
        elif page == "History Sales":
            history_sales_page()  # Display the history sales page

        # Add a text input and a "Run Query" button to the sidebar
        query = st.sidebar.text_input("Enter SQL Query")
        if st.sidebar.button("Run Query"):
            # Run the query using the function
            result = run_database_query(query)
            st.sidebar.write("Query Result:", result)

def logout():
    st.session_state.authenticated = False
    st.success("Logout successful!")

if __name__ == "__main__":
    main()
