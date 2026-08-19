import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AI Health Analyzer",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS — CLEAN GOOGLE-STYLE UI
# =========================================================
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f8f9fa;
    }

    /* Main content */
    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header */
    .hero {
        background: white;
        padding: 28px 32px;
        border-radius: 18px;
        border: 1px solid #e8eaed;
        margin-bottom: 24px;
    }

    .hero h1 {
        font-size: 38px;
        margin-bottom: 8px;
        color: #202124;
    }

    .hero p {
        color: #5f6368;
        font-size: 17px;
        margin: 0;
    }

    /* Cards */
    .card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e8eaed;
        margin-bottom: 18px;
    }

    /* Section heading */
    .section-title {
        font-size: 24px;
        font-weight: 600;
        color: #202124;
        margin: 10px 0 15px 0;
    }

    /* Result */
    .result-card {
        background: white;
        padding: 28px;
        border-radius: 20px;
        border: 1px solid #e8eaed;
        text-align: center;
        margin-top: 25px;
    }

    .result-title {
        color: #5f6368;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .result-value {
        font-size: 34px;
        font-weight: 700;
    }

    /* Disclaimer */
    .disclaimer {
        background: #fff8e1;
        border: 1px solid #f1d78c;
        border-radius: 14px;
        padding: 20px;
        margin-top: 35px;
        color: #5f4b00;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #80868b;
        font-size: 13px;
        padding: 25px 0 10px 0;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================
@st.cache_resource
def load_model():
    return joblib.load("health_risk_pipeline.pkl")


model = load_model()


# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="hero">

<h1> AI Health Analyzer</h1>

<p>
Understand your lifestyle and nutrition patterns using a machine-learning
based health-risk analysis.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# INPUT SECTION
# =========================================================
st.markdown(
    '<div class="section-title">Tell us about your daily lifestyle</div>',
    unsafe_allow_html=True
)

st.caption(
    "Enter your usual daily values. The system automatically calculates "
    "additional health indicators."
)

# ---------------------------------------------------------
# BASIC INFORMATION
# ---------------------------------------------------------
st.markdown("### 👤 Basic Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25,
        step=1
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col3:
    bmi = st.number_input(
        "BMI",
        min_value=12.0,
        max_value=50.0,
        value=22.5,
        step=0.1
    )


# ---------------------------------------------------------
# DAILY LIFESTYLE
# ---------------------------------------------------------
st.markdown("### 🏃 Daily Lifestyle")

col1, col2, col3 = st.columns(3)

with col1:
    steps = st.number_input(
        "Daily Steps",
        min_value=500,
        max_value=30000,
        value=7000,
        step=500
    )

with col2:
    sleep = st.slider(
        "Sleep (hours)",
        min_value=3.0,
        max_value=12.0,
        value=7.0,
        step=0.5
    )

with col3:
    water = st.number_input(
        "Water (litres/day)",
        min_value=0.5,
        max_value=6.0,
        value=2.0,
        step=0.1
    )


# ---------------------------------------------------------
# NUTRITION
# ---------------------------------------------------------
st.markdown("### 🥗 Daily Nutrition")

col1, col2, col3, col4 = st.columns(4)

with col1:
    calories = st.number_input(
        "Calories (kcal)",
        min_value=1000,
        max_value=5000,
        value=2000,
        step=50
    )

with col2:
    protein = st.number_input(
        "Protein (g)",
        min_value=10.0,
        max_value=250.0,
        value=60.0,
        step=1.0
    )

with col3:
    fiber = st.number_input(
        "Fiber (g)",
        min_value=5.0,
        max_value=100.0,
        value=25.0,
        step=1.0
    )

with col4:
    fat = st.number_input(
        "Fat (g)",
        min_value=10.0,
        max_value=200.0,
        value=60.0,
        step=1.0
    )


# =========================================================
# OPTIONAL ADVANCED NUTRITION
# =========================================================
with st.expander("⚙️ Advanced Nutrition (Optional)"):

    col1, col2 = st.columns(2)

    with col1:
        iron = st.number_input(
            "Iron (mg)",
            min_value=3.0,
            max_value=40.0,
            value=12.0,
            step=0.5
        )

    with col2:
        calcium = st.number_input(
            "Calcium (mg)",
            min_value=200,
            max_value=2000,
            value=900,
            step=50
        )


# =========================================================
# ACTIVITY LEVEL — AUTOMATIC
# =========================================================
if steps < 3000:
    activity_level = "Sedentary"
elif steps < 7500:
    activity_level = "Light"
elif steps < 12500:
    activity_level = "Moderate"
else:
    activity_level = "Active"


# =========================================================
# FEATURE ENGINEERING
# =========================================================

# These formulas must remain consistent with training.
calorie_adequacy = calories / 2000
protein_adequacy = protein / 60
fiber_adequacy = fiber / 30
hydration_score = water / 2.5
activity_score = steps / 8000
sleep_score = sleep / 8

# BMI risk category
if bmi < 18.5:
    bmi_risk = 1
elif bmi < 25:
    bmi_risk = 0
elif bmi < 30:
    bmi_risk = 1
else:
    bmi_risk = 2


# =========================================================
# ANALYZE BUTTON
# =========================================================
st.markdown("")

analyze = st.button(
    "🔍 Analyze My Health",
    type="primary",
    use_container_width=True
)


if analyze:

    # -----------------------------------------------------
    # INPUT DATAFRAME
    # -----------------------------------------------------
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "BMI": bmi,
        "Daily_Calories_kcal": calories,
        "Protein_g": protein,
        "Fiber_g": fiber,
        "Fat_g": fat,
        "Iron_mg": iron,
        "Calcium_mg": calcium,
        "Water_L": water,
        "Steps_Per_Day": steps,
        "Sleep_Hours": sleep,
        "Activity_Level": activity_level,

        "Calorie_Adequacy": calorie_adequacy,
        "Protein_Adequacy": protein_adequacy,
        "Fiber_Adequacy": fiber_adequacy,
        "Hydration_Score": hydration_score,
        "Activity_Score": activity_score,
        "Sleep_Score": sleep_score,
        "BMI_Risk": bmi_risk
    }])


    # -----------------------------------------------------
    # PREDICTION
    # -----------------------------------------------------
    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    classes = model.classes_

    probability_df = pd.DataFrame({
        "Risk": classes,
        "Probability": probabilities
    }).sort_values(
        "Probability",
        ascending=False
    )


    # -----------------------------------------------------
    # RISK COLORS / TEXT
    # -----------------------------------------------------
    if prediction == "Healthy":
        result_color = "#188038"
        result_icon = "🟢"

    elif prediction == "Moderate Risk":
        result_color = "#b06000"
        result_icon = "🟡"

    else:
        result_color = "#d93025"
        result_icon = "🔴"


    # -----------------------------------------------------
    # HEALTH SCORE
    # -----------------------------------------------------
    nutrition_score = np.mean([
        min(calorie_adequacy, 1),
        min(protein_adequacy, 1),
        min(fiber_adequacy, 1),
        min(calcium / 1000, 1),
        min(iron / 12, 1)
    ]) * 100

    lifestyle_score = np.mean([
        min(activity_score, 1),
        min(sleep_score, 1),
        min(hydration_score, 1)
    ]) * 100

    bmi_score = 100

    if bmi < 18.5:
        bmi_score = 65
    elif bmi < 25:
        bmi_score = 100
    elif bmi < 30:
        bmi_score = 70
    else:
        bmi_score = 45

    health_score = (
        nutrition_score * 0.40
        + lifestyle_score * 0.35
        + bmi_score * 0.25
    )

    health_score = round(
        max(0, min(100, health_score)),
        1
    )


    # =====================================================
    # RESULT
    # =====================================================
    st.markdown(
        f"""
        <div class="result-card">

        <div class="result-title">
        AI Health Risk Assessment
        </div>

        <div class="result-value"
             style="color:{result_color};">

        {result_icon} {prediction}

        </div>

        <p style="color:#5f6368;">
        Based on the lifestyle and nutrition information provided.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # SCORE + PROBABILITY
    # =====================================================
    col1, col2 = st.columns(2)

    # -----------------------------------------------------
    # Health Score
    # -----------------------------------------------------
    with col1:

        st.markdown("### ❤️ Overall Lifestyle Score")

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=health_score,
                number={
                    "suffix": "/100"
                },
                gauge={
                    "axis": {
                        "range": [0, 100]
                    },
                    "steps": [
                        {
                            "range": [0, 40],
                            "color": "#fce8e6"
                        },
                        {
                            "range": [40, 70],
                            "color": "#fef7e0"
                        },
                        {
                            "range": [70, 100],
                            "color": "#e6f4ea"
                        }
                    ],
                    "bar": {
                        "color": "#1a73e8"
                    }
                }
            )
        )

        fig.update_layout(
            height=300,
            margin=dict(
                l=20,
                r=20,
                t=30,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # -----------------------------------------------------
    # Probability
    # -----------------------------------------------------
    with col2:

        st.markdown("### 📊 Prediction Probability")

        for _, row in probability_df.iterrows():

            probability = row["Probability"] * 100

            st.write(
                f"**{row['Risk']}** — "
                f"{probability:.1f}%"
            )

            st.progress(
                float(row["Probability"])
            )


    # =====================================================
    # RISK FACTORS
    # =====================================================
    st.markdown("### 🔎 Key Lifestyle Factors")

    factors = []

    if bmi >= 30:
        factors.append("BMI is in a higher-risk range.")
    elif bmi >= 25:
        factors.append("BMI is above the generally healthy range.")

    if sleep < 6:
        factors.append("Daily sleep is below 6 hours.")

    if steps < 4000:
        factors.append("Daily activity is relatively low.")

    if water < 2:
        factors.append("Water intake is relatively low.")

    if protein_adequacy < 0.75:
        factors.append("Protein intake is below the selected reference level.")

    if fiber_adequacy < 0.70:
        factors.append("Fiber intake is below the selected reference level.")

    if not factors:
        factors.append(
            "No major lifestyle concern was detected from the entered values."
        )

    for factor in factors:

        with st.container(border=True):
            st.write("• " + factor)


    # =====================================================
    # RECOMMENDATIONS
    # =====================================================
    st.markdown("### 💡 Personalized Recommendations")

    recommendations = []

    if protein_adequacy < 0.8:
        recommendations.append(
            "Increase protein-rich foods such as pulses, dairy, eggs, tofu or other suitable sources."
        )

    if fiber_adequacy < 0.8:
        recommendations.append(
            "Add more vegetables, fruits, whole grains, legumes and other fiber-rich foods."
        )

    if steps < 5000:
        recommendations.append(
            "Gradually increase daily physical activity according to your fitness level."
        )

    if sleep < 7:
        recommendations.append(
            "Try to maintain a consistent sleep schedule and aim for adequate sleep."
        )

    if water < 2:
        recommendations.append(
            "Consider increasing fluid intake according to your personal needs and climate."
        )

    if not recommendations:
        recommendations.append(
            "Your entered lifestyle values look reasonably balanced. Continue maintaining consistent healthy habits."
        )

    for recommendation in recommendations:

        with st.container(border=True):
            st.write("✓ " + recommendation)


# =========================================================
# EDUCATIONAL DISCLAIMER
# =========================================================
st.markdown("""
<div class="disclaimer">

<b>⚠️ Educational & Prototype Disclaimer</b><br><br>

This AI Health Analyzer is developed <b>for educational, learning and
demonstration purposes only</b>. It is a machine-learning prototype and
is not a medical device, diagnostic system, or substitute for professional
medical advice.<br><br>

The prediction is based only on the information entered by the user and
may be inaccurate or incomplete. The results should not be used to
diagnose, treat, prevent, or make decisions about any medical condition.<br><br>

Health and nutrition requirements can vary significantly between
individuals. If you have symptoms, medical concerns, or receive an
unexpected result, consult a qualified healthcare professional.<br><br>

<b>Do not make medication, treatment, or emergency decisions based on
this application.</b>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">

AI Health Analyzer • Machine Learning Prototype •
Built for Educational & Demonstration Purposes

</div>
""", unsafe_allow_html=True)

# =========================================================
# PROFESSIONAL FOOTER
# =========================================================
# =========================================================
# PROFESSIONAL FOOTER
# =========================================================
st.markdown("""
<div style="
    text-align:center;
    padding:35px 10px 15px 10px;
    margin-top:40px;
    border-top:1px solid #e8eaed;
">

    <div style="
        font-size:16px;
        font-weight:600;
        color:#202124;
        margin-bottom:6px;
    ">
        ❤️ AI Health Analyzer
    </div>

    <div style="
        font-size:14px;
        color:#5f6368;
        margin-bottom:10px;
    ">
        AI-powered Lifestyle & Nutrition Risk Analysis
    </div>

    <div style="
        font-size:13px;
        color:#80868b;
        line-height:1.6;
    ">
        Designed & Developed by <b>Anshu Sahani</b><br>
        B.Tech — Artificial Intelligence & Data Science
    </div>

    <div style="
        font-size:12px;
        color:#9aa0a6;
        margin-top:12px;
    ">
        Machine Learning • Python • Streamlit • Data Science
    </div>

    <div style="
        font-size:11px;
        color:#9aa0a6;
        margin-top:8px;
    ">
        Educational Prototype • Not intended for medical diagnosis
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align:center;
    padding:38px 10px 18px 10px;
    margin-top:45px;
    border-top:1px solid #e8eaed;
">

    <div style="
        font-size:20px;
        font-weight:700;
        color:#202124;
        margin-bottom:6px;
    ">
        ❤️ AI Health Analyzer
    </div>

    <div style="
        font-size:14px;
        color:#5f6368;
        margin-bottom:18px;
    ">
        Intelligent Lifestyle, Nutrition & Health-Risk Analysis
    </div>

    <div style="
        font-size:14px;
        color:#5f6368;
        line-height:1.8;
    ">
        <b>Designed & Developed by</b><br>
        Nikita Nishad<br>
        <span style="color:#80868b;">
        Bachelor of Pharmacy (B.Pharm)
        </span>
    </div>

    <div style="
        margin-top:18px;
        font-size:12px;
        color:#80868b;
    ">
        Artificial Intelligence • Machine Learning • Pharmacy •
        Personalized Health Analytics
    </div>

    <div style="
        margin-top:14px;
        font-size:11px;
        color:#9aa0a6;
        line-height:1.6;
    ">
        AI Health Analyzer is an educational and research prototype.
        It is not intended to diagnose, treat, cure, or prevent any disease.
        Always consult a qualified healthcare professional for medical decisions.
    </div>

</div>
""", unsafe_allow_html=True)