import streamlit as st
import main

st.title("welcome to davinX")

st.sidebar.success("select a page above")

if "name" not in st.session_state:
    st.session_state["name"] = ""

if "birthday" not in st.session_state:
    st.session_state["birthday"] = 0

if "year_looking" not in st.session_state:
    st.session_state["year_looking"] = 0


name = st.text_input("input your name", st.session_state["name"])
birthday = st.text_input("input your birth day (yyyy-mm-dd)", st.session_state["birthday"])
year_looking = st.text_input("what year are you want to focast", st.session_state["year_looking"])
submit = st.button("submit")
if submit:
    st.session_state["birthday"] = birthday
    st.session_state["name"] = name
    st.session_state["year_looking"] = year_looking

    # Assume the day is stored in a variable called day
    day = birthday
    
    # Split the day by "." and assign the result to a list called parts
    parts = day.split("-")
    
    # Access the elements of the list by index and assign them to variables
    year = parts[0]
    month = parts[1]
    date = parts[2]
    
    output = main.main(date, month, year, name, year_looking)

    st.write(output)
