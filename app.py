import streamlit as st
from generator import make_excel, load_subcategories, load_states

st.title("Tax DataGen")
st.write("Generate BasicAvalara test data")


final_list = load_subcategories("data/subcategories.csv")
category = st.selectbox(
    "Select Category",
    final_list.keys())

subcategory = st.selectbox(
    "Select Subcategory",
    final_list[category])

num_transactions = st.number_input("Number of transactions", min_value=1, max_value=10000, value=10)

mode = st.radio("Mode", ["E-commerce", "Outlet"])

store_id = ""
if mode == "Outlet":
    store_id = st.text_input("Store ID")

state_list = load_states("data/uszips.csv")
state = st.selectbox("State", state_list)
county = st.text_input("County")
city = st.text_input("City")
zip_code = st.text_input("Zip Code")



