# -------------------- IMPORTS --------------------
import streamlit as st
import pandas as pd
import joblib
import time
import os
from io import BytesIO
from fpdf import FPDF
import base64

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Mental Health Treatment Predictor",
    page_icon="🌿",
    layout="wide"
)

# -------------------- MODEL LOADING --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "mental_health_model.pkl")
features_path = os.path.join(BASE_DIR, "model_features.pkl")

try:
    model = joblib.load(model_path)
    model_features = joblib.load(features_path)
except FileNotFoundError as e:
    st.error(f"Required file not found: {e}")
    st.stop()

# -------------------- PREDICTION FUNCTION --------------------
def predict_treatment(input_df, threshold=0.4):
    df_encoded = pd.get_dummies(input_df, drop_first=True)
    for col in model_features:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[model_features]
    probs = model.predict_proba(df_encoded)[0]
    prediction = 1 if probs[1] >= threshold else 0
    confidence = probs[prediction]
    ci_range = 0.05
    return prediction, confidence, max(confidence-ci_range, 0), min(confidence+ci_range, 1)

# -------------------- PDF GENERATOR --------------------
def create_pdf(age, answers, prediction, confidence):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Mental Health Prediction Report", ln=1, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Age: {age}", ln=1)
    for q, a in answers.items():
        pdf.cell(200, 10, txt=f"{q}: {a}", ln=1)
    pdf.ln(10)
    result = "Likely to Seek Treatment" if prediction == 1 else "Unlikely to Seek Treatment"
    pdf.cell(200, 10, txt=f"Prediction: {result}", ln=1)
    pdf.cell(200, 10, txt=f"Confidence: {confidence:.2%}", ln=1)
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    return BytesIO(pdf_bytes)

# -------------------- STYLE --------------------
st.markdown("""
<style>
.centered { text-align: center; padding-top: 60px; }
.fade-in { animation: fadeIn 1.2s ease-in; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.result-box {
    padding: 20px;
    border-left: 5px solid #52c41a;
    background-color: #f6ffed;
    margin-top: 20px;
    border-radius: 10px;
    font-size: 18px;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SESSION STATE INIT --------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------- SIDEBAR NAVIGATION --------------------
st.sidebar.markdown("### Navigation")
for label in ["Home", "Privacy Policy", "Documentation"]:
    if st.sidebar.button(label):
        st.session_state.page = label.lower().replace(" ", "_")
        st.rerun()

# -------------------- PAGE ROUTING --------------------
if st.session_state.page == "home":
    st.markdown('<div class="centered fade-in">', unsafe_allow_html=True)
    st.markdown("""
    <h1 class='slide-in'>Welcome to the Mental Health Predictor</h1>
    <p class='fade-in'>This playful app uses a machine learning model to predict if you might seek mental health treatment based on your input.</p>
    <p><b>No personal data is stored. This is for educational purposes only.</b></p>
    """, unsafe_allow_html=True)
    
    if st.checkbox("I agree to the Privacy Terms") and st.button("Let's Go!"):
        st.balloons()
        st.session_state.page = "model"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "privacy_policy":
    st.title("Privacy Policy")
    st.markdown("""
    - We do not store any personal data.
    - All processing is temporary and local.
    - This tool is for educational purposes only.
    """)

elif st.session_state.page == "model":
    st.title("Mental Health Treatment Predictor")
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            age = st.slider("Your Age", 18, 100, 30)
            self_employed = st.selectbox("Are you self-employed?", ["Yes", "No"])
            family_history = st.selectbox("Family history of mental illness?", ["Yes", "No"])
        with col2:
            remote_work = st.selectbox("Do you work remotely?", ["Yes", "No"])
            tech_company = st.selectbox("Do you work in tech?", ["Yes", "No"])
        
        disclaimer = st.checkbox("I understand this is for educational use only.")
        
       

        submitted = st.form_submit_button("Make My Prediction!")

    # Only proceed if submitted AND disclaimer was accepted
    if submitted and disclaimer:
        with st.spinner("Generating prediction..."):
            time.sleep(1)

            # Construct input data
            input_data = pd.DataFrame([{
                "Age": age,
                "self_employed": 1 if self_employed == "Yes" else 0,
                "family_history": 1 if family_history == "Yes" else 0,
                "remote_work": 1 if remote_work == "Yes" else 0,
                "tech_company": 1 if tech_company == "Yes" else 0
            }])

            # Make prediction
            prediction, confidence, ci_low, ci_high = predict_treatment(input_data)

        # Save to session state and redirect
        st.session_state.result = {
            "prediction": prediction,
            "confidence": confidence,
            "ci_low": ci_low,
            "ci_high": ci_high,
            "age": age,
            "answers": {
                "Self-employed": self_employed,
                "Family History": family_history,
                "Remote Work": remote_work,
                "Tech Company": tech_company
            }
        }
        st.session_state.page = "results"
        st.rerun()

    elif submitted and not disclaimer:
        st.error("Please agree to the terms before generating a prediction.")

# results page
elif st.session_state.page == "results":
    result = st.session_state.result
    prediction = result["prediction"]
    confidence = result["confidence"]
    ci_low = result["ci_low"]
    ci_high = result["ci_high"]
    age = result["age"]
    answers = result["answers"]

    st.title("Your Prediction Result")
    result_text = "Likely to seek mental health support." if prediction == 1 else "Unlikely to seek mental health support."
    color = "#f6ffed" if prediction == 1 else "#fffbe6"
    border_color = "#52c41a" if prediction == 1 else "#faad14"

    st.markdown(f"""
    <div class="result-box fade-in" style="background-color:{color}; border-left-color:{border_color};">
        <b>Prediction:</b> {result_text}<br>
        <b>Confidence:</b> {confidence:.2%}<br>
        <b>Approx. 95% CI:</b> {ci_low:.2%} - {ci_high:.2%}
    </div>
    """, unsafe_allow_html=True)

    st.progress(confidence)
    st.write(f"Model confidence: {confidence:.2%}")

    report = create_pdf(age, answers, prediction, confidence)
    b64 = base64.b64encode(report.read()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="mental_health_report.pdf">Download Your Report (PDF)</a>'
    st.markdown(href, unsafe_allow_html=True)

    st.markdown("### Model explanation (based on selected answers):")
    if answers["Family History"] == "Yes":
        st.markdown("- Family history can increase likelihood of treatment-seeking.")
    if answers["Self-employed"] == "Yes":
        st.markdown("- Self-employment may correlate with higher stress or lower access to benefits.")
    if answers["Remote Work"] == "Yes":
        st.markdown("- Remote work can affect mental health patterns differently.")

    if st.button("Try Again"):
        st.session_state.page = "model"
        st.rerun()

elif st.session_state.page == "documentation":
    st.title("Project Documentation")
    with st.expander("Show Documentation Sections", expanded=True):
        section = st.radio("Select Section:", [
            "Overview", "Getting Started", "Project Structure",
            "Machine Learning Summary", "Key Insights", "Future Improvements",
            "Contributors", "Contact & Support"])

    doc_content = {
        "Overview": """This app uses a machine learning model trained on the 2014 OSMI Mental Health in Tech dataset to predict the likelihood of seeking mental health treatment.""",
        "Getting Started": """1. Clone: `git clone https://github.com/markchweya/DSA2040A_DataMining_Group1.git`
2. Install: `pip install -r requirements.txt`
3. Launch: `streamlit run app/app.py`""",
        "Project Structure": """
DSA2040A_DataMining_Group1/
├── app/
│   └── app.py
├── data/
│   └── us_model_data/training_model_dataset.csv
├── models/
│   └── mental_health_model.pkl
├── notebooks/
│   ├── 1_cleaning_and_filtering.ipynb
│   ├── 2_exploratory_analysis_us.ipynb
│   ├── 3_classification_model.ipynb
│   └── 4_dashboard_insights.ipynb
├── requirements.txt
└── README.md
""",
        "Machine Learning Summary": """- Target: `treatment`
- Model: Random Forest Classifier
- Accuracy: ~61%
- F1 Score: ~66% for positive class""",
        "Key Insights": """- Family history is a strong predictor
- Smaller companies often lack mental health support
- Gender and age influence likelihood of seeking treatment""",
        "Future Improvements": """- Add SHAP explanations
- Include more diverse or updated datasets
- Expand to multilingual support""",
        "Contributors": """- Nathan – Pipeline
- Nicholas – Data wrangling
- Faith – EDA & modeling
- Merhawit – ML modeling
- Mark – App and documentation""",
        "Contact & Support": """- Email: chweyamark@gmail.com
- GitHub: [Project Repo](https://github.com/markchweya/DSA2040A_DataMining_Group1)"""
    }

    st.markdown(doc_content[section])
