import csv
from openpyxl import Workbook
import random


def load_subcategories(path):
    subcategories = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subcategories.append(row["Subcategory"])
    return subcategories

def random_number_amount(): 
    rate = round(random.uniform(0, 10), 2)
    gross = round(random.uniform(50, 100000), 2)
    exempt = round(random.uniform(0, gross), 2)
    taxable = round((gross - exempt), 2)
    st_collected = taxable * rate

    return gross, exempt, taxable, st_collected



def make_excel(num_transaction, state, subcategory, store_id):

    wb = Workbook()
    ws = wb.active
    ws.title = "Data import 1"


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
            "Los Angeles",
            "Los Angeles",
            "90001",
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


    output_name = "BasicAvalara_test.xlsx"
    wb.save(output_name)
    print(f"Created {output_name}")

