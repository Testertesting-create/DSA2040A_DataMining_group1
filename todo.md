# DSA 2040A Group Project – End-to-End Data Mining: Detailed TODO

## Project Overview
- **Goal:** Apply the full data pipeline (ETL → Data Mining → Insights & Storytelling) to a chosen dataset or previously cleaned data. Use mining techniques to uncover patterns, trends, and insights for decision-making.
- **Duration:** 5 Weeks
- **Submission:** GitHub Public Repository
- **Foundation:** Builds upon midterm ETL pipeline

---

## Folder Structure (Required)
- [ ] Create main project folder: `DataMining_GroupProject_<GroupMembersName>/`
    - [ ] `data/`
        - [ ] `raw/` (store original datasets)
        - [ ] `transformed/` (store cleaned/transformed data)
        - [ ] `final/` (store final datasets for mining/insights)
    - [ ] `notebooks/`
        - [ ] `1_extract_transform.ipynb` (ETL pipeline)
        - [ ] `2_exploratory_analysis.ipynb` (EDA & stats)
        - [ ] `3_data_mining.ipynb` (mining techniques)
        - [ ] `4_insights_dashboard.ipynb` (dashboard/visualization)
    - [ ] `report/`
        - [ ] `executive_summary.pdf` (1–2 page summary)
        - [ ] `presentation.pptx` (final presentation deck)
    - [ ] `requirements.txt` (all dependencies)
    - [ ] `.gitignore` (ignore data, outputs, etc. as needed)
    - [ ] `README.md` (project overview, instructions, contributions)

---

## Week 1 – Kickoff & Dataset Selection
- [ ] **Choose project topic** (e.g., e-commerce, health, finance, education)
- [ ] **Form group & assign roles:**
    - [ ] ETL lead
    - [ ] Analyst
    - [ ] Visualizer
    - [ ] Documenter
- [ ] **Finalize/expand ETL pipeline**
    - [ ] Review midterm ETL code
    - [ ] Plan improvements/expansions
- [ ] **Set up GitHub repository:**
    - [ ] Appoint one member to create repo (format: `DSA2040A_DataMining_<GroupName>`)
    - [ ] Add all members as collaborators (write access)
    - [ ] Clone repo locally (each member)
- [ ] **Draft project proposal in `README.md`:**
    - [ ] Group name, member names (first name, last 3 digits of ID)
    - [ ] Project summary (topic, questions to answer)
    - [ ] ETL summary
    - [ ] Planned techniques (stats & mining)
    - [ ] Tools to be used
    - [ ] Instructions to run notebooks
    - [ ] Team Members & Contributions section (to be updated as project progresses)

---

## Week 2 – Data Cleaning & Enrichment
- [ ] **ETL pipeline:**
    - [ ] Use ETL to produce cleaned datasets
    - [ ] Add calculated fields (e.g., profit_margin, purchase_frequency)
    - [ ] Handle outliers
    - [ ] Standardize formats (dates, categories, etc.)
    - [ ] Remove noise/irrelevant data
    - [ ] Save outputs to `data/transformed/`
- [ ] **Update `1_extract_transform.ipynb`:**
    - [ ] Document all steps with markdown/comments
    - [ ] Attribute sections to contributors (e.g., `# Section by Grace – Data Cleaning`)
- [ ] **Commit changes:**
    - [ ] Each member makes at least one commit (with clear messages)
    - [ ] Push to GitHub

---

## Week 3 – Exploratory & Statistical Analysis
- [ ] **EDA (Exploratory Data Analysis):**
    - [ ] Visualize correlations (heatmaps, pairplots)
    - [ ] Plot distributions (histograms, boxplots)
    - [ ] Group comparisons (barplots, groupby stats)
    - [ ] Use Pandas, Seaborn, Matplotlib
    - [ ] Save outputs/figures as needed
- [ ] **Update `2_exploratory_analysis.ipynb`:**
    - [ ] Document findings with markdown
    - [ ] Attribute sections to contributors
- [ ] **Commit changes:**
    - [ ] Each member makes at least one commit (with clear messages)
    - [ ] Push to GitHub

---

## Week 4 – Data Mining
- [ ] **Select 2–3 mining techniques:**
    - [ ] Clustering (e.g., k-means, DBSCAN)
    - [ ] Classification (e.g., decision trees, logistic regression)
    - [ ] Association Rules (e.g., market basket analysis)
    - [ ] Time Series (e.g., trends, forecasts)
- [ ] **Implement mining in `3_data_mining.ipynb`:**
    - [ ] Apply chosen techniques
    - [ ] Evaluate results (accuracy, support/confidence, etc.)
    - [ ] Document process and findings
    - [ ] Attribute sections to contributors
- [ ] **Commit changes:**
    - [ ] Each member makes at least one commit (with clear messages)
    - [ ] Push to GitHub

---

## Week 5 – Insight & Storytelling
- [ ] **Build mini dashboard:**
    - [ ] Use Power BI, Jupyter Dash, Seaborn, or Plotly
    - [ ] Visualize 3–5 actionable insights
    - [ ] Save dashboard in `4_insights_dashboard.ipynb`
- [ ] **Prepare executive summary:**
    - [ ] Write 1–2 page summary of findings (PDF)
    - [ ] Save as `report/executive_summary.pdf`
- [ ] **Prepare final presentation deck:**
    - [ ] Create slides with key visuals/insights
    - [ ] Save as `report/presentation.pptx`
- [ ] **Finalize `README.md`:**
    - [ ] Ensure all sections are complete
    - [ ] Update Team Members & Contributions
    - [ ] Add instructions to run all notebooks
- [ ] **Final commits & push:**
    - [ ] Each member makes at least one commit (with clear messages)
    - [ ] Push all final files to GitHub

---

## Collaboration & Contribution Rules
- [ ] **Repository ownership:**
    - [ ] Repo must be owned by a GitHub team (not individual)
    - [ ] All members added as collaborators
- [ ] **Individual contributions:**
    - [ ] Each member must make at least 3 commits (one per notebook/section)
    - [ ] Use clear commit messages (e.g., `added EDA plots - Grace`)
    - [ ] Add name to README under Team Members & Contributions
    - [ ] Comment work in notebooks (e.g., `# Section by Grace – Clustering logic here`)
- [ ] **Tracking contributions:**
    - [ ] Use GitHub Insights tab → Contributors
    - [ ] Use `git log --pretty=format:"%an - %s"` to check commit log
    - [ ] Use `git shortlog -sne` for summary (optional)
- [ ] **Penalties:**
    - [ ] One person committed everything: -20%
    - [ ] Not all names in README: -5 marks
    - [ ] No individual comments in notebooks: -5 marks
    - [ ] All contributed with evidence: Full credit

---

## Deliverables Checklist
- [ ] **GitHub repo** (public, with all folders/files)
- [ ] **Notebooks** (4 stages, in `notebooks/`)
- [ ] **Executive summary** (`report/executive_summary.pdf`)
- [ ] **Presentation** (`report/presentation.pptx`)
- [ ] **README.md** (overview, instructions, contributions)
- [ ] **requirements.txt** (all dependencies listed)
- [ ] **.gitignore** (ignore unnecessary files)

---

## README.md Must Include
- [ ] Group name, member names (first name, last 3 digits of ID)
- [ ] Project summary (topic, questions asked)
- [ ] ETL summary
- [ ] Techniques used (stats & mining)
- [ ] Tools used
- [ ] Instructions to run notebooks
- [ ] Team Members & Contributions (with clear attribution)

---

## Tips for Success
- [ ] Start each week by reviewing and dividing tasks
- [ ] Communicate regularly (meetings, chat, etc.)
- [ ] Document everything (code, markdown, comments)
- [ ] Ensure all members contribute and are credited
- [ ] Review GitHub repo for completeness before submission 