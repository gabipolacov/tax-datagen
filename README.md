Tax-DataGen

## Description
Tax-DataGen is a project to generate excel data to test an accounting app which manages tax data for companies in the United States. 
The goal of this project is generating specific data useful to test different scenarios on the app.

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

