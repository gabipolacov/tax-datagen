import streamlit as st
from generator import make_excel, load_subcategories

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

location_type = st.selectbox(
    "Select main location filter",
    ["State", "County", "City", "Zip Code"]
)

if location_type == "State":
    state_type = st.text_input("State")
elif location_type == "County":
    county_type = st.text_input("County")
elif location_type == "City":
    city_type = st.text_input("City")
elif location_type == "Zip Code":
    zip_type = st.text_input("Zip Code") 
