import csv
from openpyxl import Workbook
import random
import os

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

def validate_location(path, state=None, county=None, city=None, zip=None):
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            match_state = (not state or row["state_name"].strip().lower() == state.strip().lower())
            match_county = (not county or row["county_name"].strip().lower() == county.strip().lower())
            match_city = (not city or row["city"].strip().lower() == city.strip().lower())
            match_zip = (not zip or row["zip"] == zip)
            if match_state and match_county and match_city and match_zip:
                return True

    return False

def fill_location(path, state=None, county=None, city=None, zip=None):
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            match_state = (not state or row["state"] == state)
            match_county = (not county or row["county"] == county)
            match_city = (not city or row["city"] == city)
            match_zip = (not zip or row["zip"] == zip)

            if match_state and match_city and match_county and match_zip:
                state_output = state or row["state"]
                county_output = county or row["county"]
                city_output = city or row["city"]
                zip_output = zip or row["zip"]
                return state_output, county_output, city_output, zip_output
            
        return None


def random_number_amount(): 
    rate = round(random.uniform(0, 0.1), 4)
    gross = round(random.uniform(50, 100000), 2)
    exempt = round(random.uniform(0, gross), 2)
    taxable = round((gross - exempt), 2)
    st_collected = round((taxable * rate), 2)

    percentage = round(random.uniform(0, 0.6), 4)
    tax_purchases = round((gross * percentage), 2)
    use_tax_accrued = round((tax_purchases * rate), 2)

    return gross, exempt, taxable, st_collected, tax_purchases, use_tax_accrued

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
        gross, exempt, taxable, st_collected, tax_purchases, use_tax_accrued = random_number_amount()
        row = [
            store_id,
            state,
            county,
            city,
            zip,
            subcategory,
            gross,
            exempt,
            taxable,
            st_collected,
            tax_purchases,
            use_tax_accrued,
        ]
        ws.append(row)

    if file_name == "":
        output_name = "BasicAvalara_test.xlsx"
    else:
        output_name = file_name

    if not os.path.exists("output"):
        os.mkdir("output")

    path = os.path.join("output", output_name)
    wb.save(path)

    return output_name

