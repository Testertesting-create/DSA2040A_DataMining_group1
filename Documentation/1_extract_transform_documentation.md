# 1_extract_transform.ipynb – Data Extraction & Transformation Documentation

## Overview
This document summarizes all steps performed in the `1_extract_transform.ipynb` notebook for the OSMI Mental Health Tech Survey 2014 dataset. The goal was to extract, clean, and transform the raw survey data into a high-quality, analysis-ready format.

---

## 1. Data Extraction
- Loaded the raw dataset from the `data/raw/` folder using the correct semicolon (`;`) delimiter.
- Removed empty columns and rows caused by trailing delimiters or blank lines.
- Saved an initial cleaned version to `data/raw/OSMI_Mental_Health_Cleaned.csv`.

---

## 2. Standardizing and Inspecting Missing Values
- Defined a list of all known missing value indicators (e.g., `"NA"`, `"Not sure"`, `"Don't know"`, empty strings, etc.).
- Replaced all such values with `NaN` (the standard missing value marker in pandas) across the entire DataFrame.
- Inspected the dataset for missing values by printing the count and percentage of missing values in each column.
- Previewed a sample of rows with missing data to better understand where and how missingness occurs.

---

## 3. Data Type Conversion and Outlier Handling
- Converted the `Age` column to numeric, coercing errors to `NaN`.
- Removed rows with implausible ages (kept only ages between 15 and 80).
- Removed duplicate rows to ensure data quality.

---

## 4. Standardizing Categorical Variables
- Standardized the `Gender` column by mapping all variants to `"male"`, `"female"`, or `"other"`.
- Standardized other categorical columns (e.g., `self_employed`, `family_history`, `treatment`, etc.) to consistent lowercase values (`"yes"`, `"no"`, or `NaN`).

---

## 5. Imputing or Handling Remaining Missing Values
- For binary/categorical columns with few missing values, filled missing entries with the mode (most common value).
- For columns with moderate missingness, left as `NaN` or imputed with the mode as appropriate.
- For columns with high missingness, filled with the placeholder `"unknown"` or dropped if more than 50% missing.
- Filled missing `state` values with `"Not US"` for non-US respondents.

---

## 6. Feature Engineering
- Created an `age_group` column by binning ages into categories: `<25`, `25-34`, `35-44`, `45-54`, `55+`.

---

## 7. Saving the Cleaned Data
- Saved the fully cleaned and transformed DataFrame to `data/transformed/OSMI_Mental_Health_Final.csv`.
- Verified the final dataset had no missing values and was ready for analysis.

---

## Summary
- The extraction and transformation pipeline ensures the dataset is clean, consistent, and analysis-ready.
- All steps are reproducible and documented for transparency and team collaboration.

---

*For any questions or further clarifications, please refer to the notebook or contact the ETL lead.* 