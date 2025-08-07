Mental Health in Tech — Data Mining Project (DSA2040A)  
Course: Data Mining (DSA2040A)  
Project Title: Mining Insights from the 2014 OSMI Mental Health in Tech Survey  
Group Name: Your Group Name Here  
Institution: United States International University - Africa (USIU-A)

📋 Table of Contents  
Project Overview  
Team Members  
Objectives  
Dataset  
Methodology  
1. ETL (Extract, Transform, Load)  
2. Exploratory Data Analysis (EDA)  
3. Data Mining  
Clustering  
Classification  
Association Rule Mining  
4. Insights and Dashboard  
Results Summary  
How to Run  
Project Structure  
License

---

## 🧠 Project Overview
This project analyzes the 2014 OSMI Mental Health in Tech Survey to understand the factors that influence mental health outcomes and treatment-seeking behaviors among tech employees. The analysis involves a full data mining pipeline — from cleaning and exploration to clustering, classification, and association rule discovery.

## 👥 Team Members

| Name                        | Student ID (Last 3 Digits) | Role/Contribution              |
|-----------------------------|----------------------------|-------------------------------|
| Eliyas Kidanemariam Abraha  | 123                        | Mining & Classification Lead  |
| Merhawit Tesfay Kassa       | 456                        | EDA & Clustering Lead         |
| [Add Others]                | ...                        | Documentation, Dashboard, etc |

## 🎯 Objectives

- To identify key demographic and workplace factors associated with mental health treatment.
- To build models that can classify treatment-seeking behavior.
- To cluster similar respondent profiles.
- To discover frequent patterns using association rule mining.

## 📂 Dataset

- **Source:** OSMI Mental Health in Tech Survey (2014)
- **Attributes:** Age, Gender, Country, family history, benefits, remote work, etc.
- **Target Variable:** treatment (Yes/No)

## 🔍 Methodology

### 1. ETL (Extract, Transform, Load)  
📍 Notebook: `notebooks/1_extract_transform.ipynb`

- Cleaned gender, country, and age outliers.
- Transformed categorical variables into consistent formats.
- Created binary indicators for modeling.
- Output saved to `data/transformed/cleaned_osmi.csv`

### 2. Exploratory Data Analysis (EDA)  
📍 Notebook: `notebooks/2_exploratory_analysis.ipynb`

- Analyzed age distribution, gender balance, and country breakdown.
- Explored relationships between mental health treatment and workplace factors.
- Visualized correlations and categorical groupings using heatmaps and bar charts.

### 3. Data Mining  
📍 Notebook: `notebooks/3_data_mining.ipynb`

#### ✅ Clustering
- **Model:** KMeans Clustering
- **Goal:** Group similar individuals based on mental health-related responses.
- **Result:** Identified clusters based on remote work, family history, and workplace support.

#### ✅ Classification
- **Model:** Logistic Regression
- **Goal:** Predict whether a respondent will seek treatment based on features.
- **Performance Metrics:** Accuracy, precision, recall.

#### ✅ Association Rule Mining
- **Algorithm:** Apriori (via mlxtend)
- **Goal:** Discover rules like:  
   _If remote work = Yes and benefits = No → treatment = Yes (support: x%, confidence: y%)_

### 4. Insights and Dashboard  
📍 Notebook: `notebooks/4_insights_dashboard.ipynb` (optional/forthcoming)

- Visual storytelling using Plotly and Seaborn.
- Highlight key patterns for stakeholders (e.g., HR departments).
- 3–5 visual narratives to explain findings to a non-technical audience.

## 📊 Results Summary

| Technique         | Key Insight                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Clustering        | Employees without benefits or remote options often cluster with treatment-seekers. |
| Classification    | Logistic Regression achieved ~83% accuracy in predicting treatment behavior. |
| Association Rules | Lack of care options + family history strongly linked with seeking treatment. |

## ▶️ How to Run

### 🔧 Setup

Clone the repository:
```bash
git clone https://github.com/<your-team-name>/DataMining_GroupProject.git
cd DataMining_GroupProject
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run notebooks in order:
```bash
jupyter notebook
```
- Run: `1_extract_transform.ipynb`
- Then: `2_exploratory_analysis.ipynb`
- Then: `3_data_mining.ipynb`
- Optionally: `4_insights_dashboard.ipynb`

## 📁 Project Structure

```
DataMining_GroupProject/
├── data/
│   ├── raw/              # Original CSV dataset
│   ├── transformed/      # Cleaned dataset after preprocessing
│   └── final/            # Datasets used for mining and dashboarding
│
├── notebooks/
│   ├── 1_extract_transform.ipynb
│   ├── 2_exploratory_analysis.ipynb
│   ├── 3_data_mining.ipynb
│   └── 4_insights_dashboard.ipynb
│
├── report/
│   ├── executive_summary.pdf
│   └── presentation.pptx
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 📜 License

This project is for educational use under the United States International University – Africa (USIU-A) academic code. Dataset © OSMI.
