# 1_extract_transform.ipynb – Detailed Line-by-Line Documentation

---

## Data Cleaning Steps Overview

```markdown
## **Data Cleaning Steps Overview**

 1. **Read the raw file** using the correct delimiter (`;`).
 2. **Remove empty columns and rows** to handle any trailing semicolons or blank lines.
 3. **Save the cleaned data** to the `data/raw/` folder.
 4. **Preview the results** by printing the shape and the first few rows of the cleaned dataset.
```
**Explanation:**
- This Markdown cell provides a high-level summary of the initial data cleaning process. It helps orient the reader to the main steps that will be performed before any analysis.

---

## Data Extraction and Initial Cleaning

```python
import pandas as pd

# Path to the raw dataset
raw_path = 'C:/Users/HP/iCloudDrive/school/DSA 2040/Project/DSA2040A_DataMining_group1/OSMI Mental Health Tech Survey 2014 Dataset.csv'
cleaned_path = '../data/raw/OSMI_Mental_Health_Cleaned.csv'

# 1. Read the raw CSV with the correct delimiter
df = pd.read_csv(raw_path, delimiter=';', dtype=str)

# 2. Remove any columns that are completely empty (sometimes caused by trailing delimiters)
df = df.dropna(axis=1, how='all')

# 3. Remove any rows that are completely empty
df = df.dropna(axis=0, how='all')

# 4. Save the cleaned file (still semicolon-delimited for now)
df.to_csv(cleaned_path, index=False, sep=';')

# 5. Preview the data
print("Shape:", df.shape)
print(df.head())
```
**Explanation:**
- `import pandas as pd`: Imports the pandas library, which is essential for data manipulation and analysis in Python.
- `raw_path` and `cleaned_path`: Define the file paths for the raw input data and the cleaned output data. This makes the code flexible and easy to update if file locations change.
- `pd.read_csv(raw_path, delimiter=';', dtype=str)`: Reads the raw CSV file using a semicolon as the delimiter. All columns are read as strings to avoid type inference issues and to make cleaning easier.
- `df.dropna(axis=1, how='all')`: Removes columns that are completely empty (all values are NaN). This often happens if there are trailing delimiters in the CSV.
- `df.dropna(axis=0, how='all')`: Removes rows that are completely empty (all values are NaN). This can occur if there are blank lines in the file.
- `df.to_csv(cleaned_path, index=False, sep=';')`: Saves the cleaned DataFrame to a new CSV file, still using semicolons as the delimiter. This preserves the cleaned structure for the next steps.
- `print("Shape:", df.shape)`: Prints the number of rows and columns in the cleaned DataFrame, which is useful for verifying that the cleaning steps worked as expected.
- `print(df.head())`: Prints the first five rows of the cleaned DataFrame, providing a quick preview of the data after initial cleaning.

---

## Data Transformation Overview

```markdown
 ## 2. Data Transformation
 In this step, we will perform the following data transformation tasks:
  - Standardize column names (e.g., make lowercase, replace spaces with underscores)
  - Normalize categorical values (e.g., gender, country)
  - Handle missing values appropriately
  - Convert data types where necessary (e.g., age to integer)
  - Create any new features if needed for analysis
  - Save the transformed data for further analysis
```
**Explanation:**
- This Markdown cell outlines the goals for the transformation phase, including standardization, normalization, missing value handling, type conversion, feature engineering, and saving. It helps the reader understand the broader plan for preparing the data.

---

## Standardize Missing Values (Section Header)

```markdown
## 2.1 Standardize Missing Values
```
**Explanation:**
- This section header marks the beginning of the missing value standardization process, making the notebook easy to navigate.

---

## Standardize and Inspect Missing Values

```python
import numpy as np

# 1. Define all known missing value indicators
missing_vals = ['NA', 'N/A', 'n/a', 'na', 'Not sure', "Don't know", '', ' ']

# 2. Replace all such values with np.nan across the entire DataFrame
df_clean = df.replace(missing_vals, np.nan)

# 3. View missing value counts per column
print("Missing values per column:")
print(df_clean.isnull().sum())

# 4. View total missing values in the dataset
print(f"\nTotal missing values in dataset: {df_clean.isnull().sum().sum()}")

# 5. (Optional) View percentage of missing values per column
print("\nPercentage of missing values per column:")
print((df_clean.isnull().mean() * 100).round(2))

# 6. Show a sample of rows with missing data
print("\nSample rows with missing data:")
print(df_clean[df_clean.isnull().any(axis=1)].head())
```
**Explanation:**
- `import numpy as np`: Imports numpy, which provides the `np.nan` value used to represent missing data in pandas.
- `missing_vals = [...]`: Lists all the different ways missing data might be represented in the dataset, including various spellings and empty strings.
- `df.replace(missing_vals, np.nan)`: Replaces all instances of the listed missing value indicators with `np.nan` throughout the DataFrame, standardizing missing data representation.
- `print(df_clean.isnull().sum())`: Prints the number of missing values in each column, helping to identify which columns need further cleaning or imputation.
- `print(df_clean.isnull().sum().sum())`: Prints the total number of missing values in the entire DataFrame, giving a sense of the overall data quality.
- `print((df_clean.isnull().mean() * 100).round(2))`: Prints the percentage of missing values per column, which is useful for deciding whether to impute or drop columns.
- `print(df_clean[df_clean.isnull().any(axis=1)].head())`: Shows a sample of rows that have at least one missing value, providing concrete examples of missingness in the data.

---

## Age Cleaning (Section Header)

```markdown
# # 2.2 Here we clean the 'Age' column:
 Convert the 'Age' column to numeric values, setting any invalid entries to NaN.
- Remove rows where age is outside the range 15 to 80.
- Count and report how many rows were removed due to implausible ages.
- Check for duplicate rows, remove them if found, and report how many were removed.
- Finally, display information and a preview of the cleaned DataFrame.
```
**Explanation:**
- This Markdown cell describes the plan for cleaning the `Age` column, including type conversion, outlier removal, duplicate removal, and data preview. It helps the reader understand the rationale for each step.

---

## Clean Age, Remove Outliers, Remove Duplicates

```python
# 1. Convert Age to numeric, coerce errors to NaN
df_clean['Age'] = pd.to_numeric(df_clean['Age'], errors='coerce')

# 2. Remove age outliers (keep ages between 15 and 80)
before = len(df_clean)
df_clean = df_clean[(df_clean['Age'] >= 15) & (df_clean['Age'] <= 80)]
after = len(df_clean)
print(f"Removed {before - after} rows with implausible ages.")

# 3. (Optional) Check for duplicates and remove them
dupes = df_clean.duplicated().sum()
if dupes > 0:
    df_clean = df_clean.drop_duplicates()
    print(f"Removed {dupes} duplicate rows.")

# 4. Preview the cleaned data
print(df_clean.info())
print(df_clean.head())
```
**Explanation:**
- `pd.to_numeric(df_clean['Age'], errors='coerce')`: Converts the `Age` column to numeric values. Any value that cannot be converted (e.g., text, symbols) is set to `NaN`, ensuring only valid numbers remain.
- `df_clean[(df_clean['Age'] >= 15) & (df_clean['Age'] <= 80)]`: Filters the DataFrame to keep only rows where age is between 15 and 80, removing outliers and likely data entry errors.
- `before` and `after`: Store the number of rows before and after filtering, allowing the code to report how many rows were removed as outliers.
- `df_clean.duplicated().sum()`: Counts the number of duplicate rows in the DataFrame.
- `df_clean.drop_duplicates()`: Removes duplicate rows, ensuring each survey response is unique.
- `print(df_clean.info())`: Prints a summary of the DataFrame, including the number of non-null values and data types for each column.
- `print(df_clean.head())`: Shows the first five rows of the cleaned DataFrame, providing a final preview after cleaning.

---

*This documentation covers the extraction, initial cleaning, missing value standardization, and age cleaning steps. For further steps (categorical standardization, imputation, feature engineering, saving), continue in this style for the rest of the notebook.* 