import csv
from openpyxl import Workbook


def load_subcategories(path):
    subcategories = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subcategories.append(row["Subcategory"])
    return subcategories

def random_number_amount(): 
    gross = round(random.uniform(50, 10000000), 2)
    exempt = round(random.uniform(50, gross), 2)
    taxable = round(gross - exempt), 2

    return gross, exempt, taxable



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
        "Gross Sales"
        "Exempt sales",
        "Taxable sales",
        "Tax Collected",
        "Taxable purchases",
        "Use tax accrued",
    ]
    ws.append(headers)

    for t in range(num_transaction):
        row = [
            store_id,              # E-commerce → blank Store Id
            state,
            "Los Angeles",
            "Los Angeles",
            "90001",
            subcategory,
            100.00,
            20.00,
            80.00,
            6.40,
            0.00,
            0.00,
            0.00,
        ]
        ws.append(row)


    output_name = "BasicAvalara_test.xlsx"
    wb.save(output_name)
    print(f"Created {output_name}")

