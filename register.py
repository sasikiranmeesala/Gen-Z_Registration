import streamlit as st
import mysql.connector

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Hitesh#0707",
        database="miracle_hackthon"
    )

# Function to create tables if they don't exist
def create_tables():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS mentors (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

    connection.commit()
    connection.close()

# Function to register a mentor
def register_mentor(username, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    sql = "INSERT INTO mentors (username, password) VALUES (%s, %s)"
    val = (username, password)
    cursor.execute(sql, val)

    connection.commit()
    connection.close()

# Function to register a student
def register_student(username, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    sql = "INSERT INTO students (username, password) VALUES (%s, %s)"
    val = (username, password)
    cursor.execute(sql, val)

    connection.commit()
    connection.close()

# Function to display mentor registration form
def mentor_registration():
    st.header("Mentor Registration")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        register_mentor(username, password)
        st.success("Registration successful!")

# Function to display student registration form
def student_registration():
    st.header("Student Registration")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        register_student(username, password)
        st.success("Registration successful!")

# Main function
def main():
    create_tables()
    page = st.sidebar.radio("Select Page", ("Mentor Registration", "Student Registration"))

    if page == "Mentor Registration":
        mentor_registration()

    elif page == "Student Registration":
        student_registration()

if __name__ == "__main__":
    main()
