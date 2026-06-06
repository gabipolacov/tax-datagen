import csv
from openpyxl import Workbook
import random

def load_subcategories(path):

    final_list = {}
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            category = row["Category"]
            subcategory = row["Subcategory"]
            if category not in final_list:
                final_list[category] = [subcategory]
            else:
                final_list[category].append(subcategory)
    return final_list

def load_states(path):
    state_list = set()
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            state_list.add(row["state_name"])
    return sorted(state_list)

def validate_location(path, state, county=None, city=None, zip=None):
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            match_state = (state == None or row["state_name"].strip().lower() == state.strip().lower())
            match_county = (county == None or row["county_name"].strip().lower() == county.strip().lower())
            match_city = (city == None or row["city"].strip().lower() == city.strip().lower())
            match_zip = (zip == None or row["zip"] == zip)
            if match_state and match_county and match_city and match_zip:
                return True

    return False


def random_number_amount(): 
    rate = round(random.uniform(0, 10), 2)
    gross = round(random.uniform(50, 100000), 2)
    exempt = round(random.uniform(0, gross), 2)
    taxable = round((gross - exempt), 2)
    st_collected = taxable * rate

    return gross, exempt, taxable, st_collected

def make_excel(subcategory, num_transaction, state, file_name=None, store_id=None, county=None, city=None, zip=None):

    wb = Workbook()
    ws = wb.active
    ws.title = "Data import"

    headers = [
        "Store Id",
        "State",
        "County",
        "City",
        "Zip Code",
        "Subcategory",
        "Gross Sales",
        "Exempt sales",
        "Taxable sales",
        "Tax Collected",
        "Taxable purchases",
        "Use tax accrued",
    ]
    ws.append(headers)

    for t in range(num_transaction):
        gross, exempt, taxable, st_collected = random_number_amount()
        row = [
            store_id,              # E-commerce → blank Store Id
            state,
            county,
            city,
            zip,
            subcategory,
            gross,
            exempt,
            taxable,
            st_collected,
            0.00,
            0.00,
            0.00,
        ]
        ws.append(row)

    if file_name == "":
        output_name = "BasicAvalara_test.xlsx"
    else:
        output_name = file_name

    wb.save(output_name)
    print(f"Created {output_name}")

