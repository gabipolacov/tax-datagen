import streamlit as st
from generator import make_excel, load_subcategories, load_states, validate_location

st.title("Tax DataGen")
st.write("Generate BasicAvalara test data")

st.divider()

final_list = load_subcategories("data/subcategories.csv")
category = st.selectbox(
    "Select Category",
    final_list.keys())

subcategory = st.selectbox(
    "Select Subcategory",
    final_list[category])

st.divider()

num_transactions = st.number_input("Number of transactions", min_value=1, max_value=10000, value=10)

st.divider()

mode = st.radio("Mode", ["E-commerce", "Outlet"])
store_id = ""
if mode == "Outlet":
    store_id = st.text_input("Store ID")

st.divider()

state_list = load_states("data/uszips.csv")
state = st.selectbox("State", state_list)
county = st.text_input("County")
city = st.text_input("City")
zip_code = st.text_input("Zip Code")

generate_button = st.button("Generate")

if generate_button.click():
    validate_location(state, county, city, zip_code)

    if validate_location() is False:
        st.error('Your location inputs do not match. Please review them.', icon="🚨")
    else
     output_name = make_excel(subcategory, num_transactions, store_id, state, county, city, state, zip_code)
     st.success('{output_name} has been generated successfully.', icon="✅")

