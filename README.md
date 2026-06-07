Tax-DataGen

## Description

Tax-DataGen is a Streamlit-based application that generates synthetic tax transaction data for testing an accounting system used by companies in the United States.

This project is an MVP designed to produce structured datasets for validating different business and tax scenarios.

The goal is to generate realistic and configurable test data to support application testing and edge-case validation.



## 🧰 Technologies Used
- Python 3.11
- Streamlit
- OpenPyXL
- CSV module
- Docker



## 🌐 External API
This project uses the Zippopotam API to validate ZIP codes and ensure consistency between ZIP codes and states.

- API used: https://api.zippopotam.us/us/{zip}
- Purpose:
  - Validate if a ZIP code exists
  - Verify that the ZIP code matches the selected state



## 📁 Project Structure

app.py
generator.py
api_utils.py
data/
  uszips.csv
  subcategories.csv
output/
README.md
requirements.txt
Dockerfile

- app.py: Streamlit user interface (UI layer)
- generator.py: Core backend logic (data processing, validation, and Excel generation)
- api_utils.py: External API utilities (ZIP code validation)
- data/uszips.csv: Dataset containing state, county, city, and ZIP code mappings
- data/subcategories.csv: Dataset containing product tax categories and subcategories
- output/: Directory where generated Excel files are saved
- README.md: Project documentation and setup instructions
- requirements.txt: List of Python dependencies required to run the application inside a virtual environment or Docker container
- Dockerfile: Configuration file that defines how to build the Docker image, including installing dependencies and running the Streamlit application



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


## ▶️ How to run and use the Application with Docker

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_FOLDER>
```

---

### 2. Build the Docker image

Make sure Docker is installed and running, then execute:

```bash
docker build -t tax-datagen .
```

---

### 3. Run the container

```bash
docker run -p 8501:8501 tax-datagen
```

---

### 4. Open the application

Go to the following URL in your browser:

```
http://localhost:8501
```

---

## ⚠️ Notes

* Ensure Docker Desktop is running before executing commands
* Port **8501** must be available
* Generated files will be saved in the `/output` directory


## 5. Configure the data

   * Select a **Category** and **Subcategory**
   * Choose the **number of transactions**
   * Select **Mode** (E-commerce or Outlet)
   * (Optional) Enter a **Store ID** if using Outlet mode

---

# 6. Enter location data (flexible)

   You can provide:

   * Only **State**
   * **State + County**
   * Only **ZIP code**
   * Or full location (State, County, City, ZIP)

   The system will attempt to complete missing fields automatically.

---

# 7. ZIP validation (if provided)

   * If a ZIP code is entered, it will be validated using an external API
   * The ZIP must exist and match the selected state

---

# 8. Generate the file

   * Enter a file name
   * Click **Generate**

---

# 9. Retrieve the output

   * The Excel file will be saved in the `/output` folder
   * It will contain synthetic tax transaction data based on your inputs




