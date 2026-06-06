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

num_transaction = st.number_input("Number of transactions", min_value=1, max_value=10000, value=10)

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

st.divider()
file_name = st.text_input("File name") + ".xlsx"
generate_button = st.button("Generate")

if generate_button:
    validation = validate_location("data/uszips.csv", state, county, city, zip_code)

    if validation is False:
        st.error('Your location inputs do not match. Please review them.', icon="🚨")
    else:
     output_name = make_excel(subcategory, num_transaction, state, file_name, store_id, county, city, zip_code)
     st.success('{output_name} has been generated successfully.', icon="✅")

