from openpyxl import Workbook

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
    "Gross sales",
    "Exempt sales",
    "Taxable sales",
    "Tax Collected",
    "Taxable purchases",
    "Use tax accrued",
]
ws.append(headers)

num_transactions = 10

for t in range(num_transactions):
    row = [
        "",              # E-commerce → blank Store Id
        "CA",
        "Los Angeles",
        "Los Angeles",
        "90001",
        "Sample Subcategory",
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