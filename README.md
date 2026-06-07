Tax-DataGen

## Description

Tax-DataGen is a Streamlit-based application that generates synthetic tax transaction data for testing an accounting system used by companies in the United States.

This project is an MVP designed to produce structured datasets for validating different business and tax scenarios.

The goal is to generate realistic and configurable test data to support application testing and edge-case validation.

---

## 🧰 Technologies Used
- Python 3.11
- Streamlit
- OpenPyXL
- CSV module
- Docker

---

## 🌐 External API
This project uses the Zippopotam API to validate ZIP codes and ensure consistency between ZIP codes and states.

- API used: https://api.zippopotam.us/us/{zip}
- Purpose:
  - Validate if a ZIP code exists
  - Verify that the ZIP code matches the selected state

---

## 📁 Project Structure
.
├── app.py 
├── generator.py
├── api_utils.py
├── data/
│ ├── uszips.csv
│ └── subcategories.csv
├── output/ 
├── Dockerfile
├── requirements.txt
└── README.md

- app.py: Streamlit user interface (UI layer)
- generator.py: Core backend logic (data processing, validation, and Excel generation)
- api_utils.py: External API utilities (ZIP code validation)
- data/uszips.csv: Dataset containing state, county, city, and ZIP code mappings
- data/subcategories.csv: Dataset containing product tax categories and subcategories
- output/: Directory where generated Excel files are saved
- README.md: Project documentation and setup instructions

--- 

## 📊 Features

- **Dynamic location selection**
  - Cascading dropdowns for State → County → City based on CSV data
  - Allows partial selection of location fields

- **ZIP code validation**
  - Uses the Zippopotam API to verify if a ZIP code exists
  - Ensures the ZIP code matches the selected state

- **Flexible input handling**
  - Users can provide partial or full location data:
    - State only
    - State + City
    - ZIP code only
    - Full location (State, County, City, ZIP)
  - System attempts to resolve missing fields when possible

- **Synthetic tax data generation**
  - Generates randomized transaction data for testing purposes
  - Includes:
    - Gross sales
    - Exempt sales
    - Taxable sales
    - Tax collected
    - Taxable purchases
    - Use tax accrued

- **Configurable transactions**
  - User can define the number of transactions to generate

- **Category and subcategory selection**
  - Loads product tax categories and subcategories from CSV files

- **Store mode support**
  - Supports E-commerce and Outlet modes
  - Optional Store ID input for Outlet mode

- **Automatic file generation**
  - Creates `.xlsx` files using OpenPyXL
  - Saves output files into the `/output` directory
  - Supports custom file naming

- **Interactive Streamlit interface**
  - Simple web UI for generating datasets without writing code
  - Provides real-time validation messages and feedback

  ## 🚀 Future Improvements

- **Improved location resolution randomness**
  - The current `fill_location` function returns the first matching row when completing missing location fields.
  - A future improvement would be to randomly select from all valid matching rows to generate more diverse and realistic datasets.

- **Dynamic tax rate configuration**
  - Integrate an external tax rate API or configuration file.
  - Allow tax rates to vary based on region, improving realism in generated financial data.

- **Multi-state and mixed data generation**
  - Enable generation of datasets that include multiple states in a single file.
  - Support mixing different transaction types such as e-commerce and outlet data within the same output.

- **Advanced store and company structure**
  - Introduce support for parent company.
  - Each company could have its Filing calendar and multiple outlets
  - Each structure would be organized in separate Excel tabs for better separation and reporting.


## Getting Started

1. **Clone the GitHub repo**

   ```powershell
   git clone https://github.com/YOUR_USERNAME/tax-datagen.git
   cd tax-datagen
   ```

   Replace `YOUR_USERNAME` with your GitHub username.

2. **Install Python**

   Install Python 3.10+ from [python.org](https://www.python.org/downloads/). During setup, check **“Add Python to PATH”**.

   Verify the installation:

   ```powershell
   python --version
   ```

3. **Open a terminal in the repo folder**

   If you are not already there:

   ```powershell
   cd C:\tax-datagen
   ```

4. **Create and activate the virtual environment**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

   When active, your prompt should start with `(venv)`.

5. **Install openpyxl**

   ```powershell
   pip install openpyxl
   ```

6. **Generate the Excel file**

   ```powershell
   python make_excel.py
   ```

   This creates `BasicAvalara_test.xlsx` in the project folder.




## Instructions

- This project works with BasicAvalara template. So the data to fill is: 
Store Id: Store Id column is blank if the transaction is e-commerce. If not, Store ID should be provided by the user.

State: User is able to select any number of states of United States or all of the states.

County: should match with State.

City: Should match with County and State.

Zip Code: should match with city, county and state.
User is able to choose which data should be mandatory one:
- If user chooses State, then county, city and zip code should match state(s) selected.
- If user chooses county, then state, city and zip code should match county(ies) selected.
- If user chooses city, then state, county and zip code should match city(ies) selected.
- If user chooses zip, then county, city and state should match zip(s) selected.


Another field is subcategory which I have in a separate file.

Then we have number fields.
- Gross sales = exempt sales + taxable sales
- Exempt sales = gross sales - taxable sales
- Taxable sales =  gross sales - exempt sales
- Sales Tax Collected
- Taxable purchases
- Use tax accrued

User should be able to choose number of transactions.

User should be able to select e-commerce or outlet mode. Outlet mode will provide a Store Id, ecommerce means that store ID will be blank.

