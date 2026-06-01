import csv
from openpyxl import Workbook


def load_subcategories(path):
    subcategories = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subcategories.append(row["Subcategory"])
    return subcategories

if __name__ == "__main__":
    subs = load_subcategories("data/subcategories.csv")
    print(subs[:5])   # first 5 only
    print(f"Total: {len(subs)}")

