🩺 AI Health Companion

AI-Powered Health Risk Analysis, Nutrition & Lifestyle Intelligence Platform

An AI-powered health analytics platform that combines Machine Learning, nutrition analytics, lifestyle assessment, and explainable insights to estimate overall health-risk levels.

Live Demo: 🚀 Try AI Health Companion

⸻

📌 Overview

AI Health Companion is an educational and research-oriented health analytics application designed to analyze lifestyle, nutrition, and basic health-related parameters using Machine Learning.

The application evaluates multiple factors such as:

* BMI
* Age
* Sleep duration
* Physical activity
* Hydration
* Daily calories
* Protein intake
* Fiber intake
* Lifestyle patterns
* Other nutrition and wellness indicators

Based on these features, the system classifies users into three risk categories:

🟢 Healthy
🟡 Moderate Risk
🔴 High Risk

The goal is to demonstrate how Artificial Intelligence, Machine Learning, Nutrition Analytics, and Preventive Health Analytics can be combined into an interactive application.

⸻

🎯 Project Objectives

The main objectives of this project are:

* Build an ML-based health-risk classification system.
* Analyze nutrition and lifestyle patterns.
* Perform automated feature engineering.
* Generate health-risk probabilities.
* Calculate an overall lifestyle score.
* Identify major lifestyle risk factors.
* Provide personalized wellness recommendations.
* Demonstrate explainable Machine Learning.
* Build an interactive and user-friendly dashboard.
* Explore the intersection of Pharmacy + AI/ML + Preventive Health Analytics.

⸻

🚀 Key Features

🤖 Machine Learning Risk Prediction

Uses supervised Machine Learning to classify users into:

Risk Level	Description
🟢 Healthy	Lower estimated lifestyle-related risk
🟡 Moderate Risk	Some lifestyle factors may require improvement
🔴 High Risk	Multiple risk-related factors detected

⸻

📊 Prediction Probability

The application provides probability scores for each predicted category.

Example:

Healthy        → 72%
Moderate Risk  → 21%
High Risk      → 7%

This provides more information than simply displaying a single predicted class.

⸻

🧮 Lifestyle Score

A customized lifestyle score evaluates important wellness dimensions such as:

* Sleep
* Physical activity
* Hydration
* Protein intake
* Fiber intake
* Calorie balance
* BMI
* Overall lifestyle habits

The score helps users understand their overall lifestyle quality.

⸻

🔍 Risk Factor Analysis

The system identifies lifestyle and nutrition factors that may contribute to the estimated risk.

Example:

Potential Risk Factors
• Low physical activity
• Insufficient sleep
• Low fiber intake
• Poor hydration

⸻

💡 Personalized Recommendations

The application generates lifestyle-oriented recommendations based on the user’s inputs.

Examples:

Increase daily physical activity.
Maintain a consistent sleep schedule.
Improve hydration habits.
Include more fiber-rich foods in your diet.

Recommendations are educational and should not be interpreted as medical treatment.

⸻

📈 Interactive Visualizations

The dashboard uses Plotly and Streamlit to display:

* Risk probability charts
* Lifestyle score
* Nutrition analysis
* Health indicators
* Risk-factor summaries
* Comparative visualizations

⸻

🧠 Machine Learning Pipeline

                    USER INPUT
                        │
                        ▼
              ┌──────────────────┐
              │ Data Validation   │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Feature          │
              │ Engineering      │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Preprocessing    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ ML Classification│
              │ Model            │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Risk Probability │
              └────────┬─────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Risk Category       Lifestyle Score
             │                   │
             └─────────┬─────────┘
                       ▼
              ┌──────────────────┐
              │ Explainable      │
              │ Insights         │
              └────────┬─────────┘
                       │
                       ▼
              Personalized
              Recommendations

⸻

🤖 Machine Learning

This project uses a supervised multi-class classification approach.

Models Explored

The following algorithms were evaluated:

* Logistic Regression
* Random Forest
* Gradient Boosting
* Extra Trees
* HistGradientBoosting

After comparative evaluation and cross-validation, Random Forest was selected as the final model.

Why Random Forest?

Random Forest was selected because it:

* Handles nonlinear relationships effectively.
* Works well with mixed feature patterns.
* Provides feature importance.
* Is relatively robust against overfitting.
* Performs well for tabular datasets.
* Supports multi-class classification.

⸻

📊 Model Evaluation

The model evaluation process includes:

* Accuracy
* Precision
* Recall
* F1-Score
* Cross-validation
* Confusion Matrix
* Model comparison

Example evaluation table:

Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	—	—	—	—
Random Forest	—	—	—	—
Gradient Boosting	—	—	—	—
Extra Trees	—	—	—	—
HistGradientBoosting	—	—	—	—

Replace the — values with the actual metrics generated during model evaluation. Do not use fabricated performance numbers.

⸻

🔬 Feature Engineering

Feature engineering is used to transform raw user inputs into meaningful analytical variables.

Examples include:

BMI Category

Underweight
Normal
Overweight
Obese

Sleep Assessment

Sleep duration is evaluated against predefined wellness ranges.

Hydration Assessment

Daily water intake is analyzed relative to user characteristics and lifestyle.

Nutrition Indicators

The application evaluates:

* Calories
* Protein
* Fiber
* Other nutrition-related parameters

Activity Assessment

Physical activity is converted into analytical indicators used by the prediction system.

⸻

🧠 Explainable AI

One of the major goals of this project is to make Machine Learning predictions easier to understand.

Instead of displaying only:

Prediction: Moderate Risk

the application aims to explain:

Prediction: Moderate Risk
Important contributing factors:
1. Low physical activity
2. Insufficient sleep
3. Low fiber intake
4. Poor hydration

This approach helps users understand the relationship between their lifestyle inputs and the model’s output.

⸻

📱 Application Screens

🏠 Health Assessment Dashboard

⸻

📊 Risk Prediction

⸻

📈 Analytics Dashboard

⸻

🧠 Architecture

Add your actual screenshots inside the assets/ directory.

⸻

🛠️ Tech Stack

Programming Language

* Python

Data Science

* Pandas
* NumPy

Machine Learning

* Scikit-learn
* Random Forest
* Gradient Boosting
* Extra Trees
* HistGradientBoosting
* Logistic Regression

Visualization

* Plotly
* Streamlit

Model Management

* Joblib

Development

* Jupyter Notebook
* VS Code
* Git
* GitHub

⸻

📂 Project Structure

AI-Health-Companion/
│
├── app.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── data/
│   └── health_dataset.csv
│
├── models/
│   ├── health_risk_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Training.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── prediction.py
│   ├── recommendations.py
│   └── visualization.py
│
├── assets/
│   ├── dashboard.png
│   ├── prediction.png
│   ├── analytics.png
│   └── architecture.png
│
└── tests/
    └── test_prediction.py

⸻

⚙️ Installation

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/AI-Health-Companion.git

2. Navigate to the Project

cd AI-Health-Companion

3. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

5. Run the Application

streamlit run app.py

The application will open in your browser.

⸻

📦 Requirements

Example requirements.txt:

streamlit
pandas
numpy
scikit-learn
plotly
joblib

For reproducible environments, pin package versions after testing the application:

pip freeze > requirements.txt

⸻

🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

Recommended deployment workflow:

GitHub Repository
        ↓
Streamlit Cloud
        ↓
Live Web Application

Add your deployed application URL above in the Live Demo section.

⸻

🔐 Data Privacy

This project is designed as an educational prototype.

The application should not be used to collect, store, or process sensitive personal health information without appropriate security, privacy, consent, and regulatory controls.

For a production implementation, additional measures would be required, including:

* Secure authentication
* Encryption
* Access control
* Secure data storage
* Audit logging
* Privacy compliance
* Proper consent management

⸻

⚠️ Medical Disclaimer

AI Health Companion is an educational and research prototype.

It is:

* ❌ Not a medical device
* ❌ Not a diagnostic system
* ❌ Not a replacement for a healthcare professional
* ❌ Not intended to prescribe medication
* ❌ Not intended to provide emergency medical advice

The predictions generated by the Machine Learning model may be inaccurate or affected by limitations in the dataset, feature design, and model performance.

Users should consult qualified healthcare professionals for medical concerns, diagnosis, treatment, or medication-related decisions.

⸻

🎓 Academic Context

This project explores the intersection of:

Pharmacy
   +
Artificial Intelligence
   +
Machine Learning
   +
Nutrition Analytics
   +
Preventive Health
   +
Data Science

The project demonstrates how computational methods can be applied to analyze lifestyle and nutrition-related data in an educational environment.

⸻

🔮 Future Improvements

The project can be extended with:

🧠 Advanced AI

* SHAP-based explainability
* XGBoost / LightGBM comparison
* Hyperparameter optimization
* Automated model selection
* Model monitoring

🏥 Health Analytics

* More health indicators
* Longitudinal health tracking
* Personalized wellness trends
* Risk history
* Progress tracking

🥗 Nutrition Intelligence

* Personalized meal recommendations
* Macro tracking
* Micronutrient analysis
* Food database integration
* Calorie and protein optimization

🤖 AI Assistant

Future versions can include an AI health-information assistant capable of:

* Explaining health metrics
* Explaining model predictions
* Answering general wellness questions
* Providing educational information

📊 Dashboard

Future dashboard features:

* User profiles
* Historical predictions
* Interactive trend charts
* Risk progression
* Goal tracking
* Downloadable reports

🔐 Production Readiness

* Authentication
* Database integration
* API backend
* Secure deployment
* Automated testing
* CI/CD
* Monitoring

⸻

🧪 Testing

Testing can be implemented using:

pytest

Example:

pytest tests/

Potential test cases include:

* Input validation
* BMI calculation
* Feature engineering
* Prediction output
* Probability calculation
* Risk classification
* Recommendation generation

⸻

📌 Limitations

The current version has several limitations:

* Model performance depends heavily on dataset quality.
* Predictions are not clinical diagnoses.
* Lifestyle factors may not capture every aspect of individual health.
* The dataset may not represent all populations.
* Correlation in the dataset does not necessarily imply causation.
* Recommendations are educational rather than medical.

⸻

🚀 Roadmap

[x] Basic health-risk prediction
[x] Random Forest classification
[x] Nutrition analysis
[x] Lifestyle scoring
[x] Streamlit dashboard
[x] Risk probability
[x] Personalized insights
[ ] SHAP explainability
[ ] User history
[ ] Database integration
[ ] AI health assistant
[ ] Advanced nutrition engine
[ ] Authentication
[ ] REST API
[ ] Automated testing
[ ] CI/CD
[ ] Production deployment

⸻

👨‍💻 Author

Anshu Sahani

B.Tech — Artificial Intelligence & Data Science

Interested in:

* Data Science
* Machine Learning
* Artificial Intelligence
* Health Analytics
* Nutrition Intelligence
* Explainable AI

⸻

⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

⸻

📄 License

This project is licensed under the MIT License.

See the LICENSE file for more information.

⸻

⚕️ Final Note

AI Health Companion demonstrates how Machine Learning can be integrated with lifestyle and nutrition analytics to create an interactive preventive-health research prototype.

The project is intended to demonstrate AI/ML engineering, data science, feature engineering, visualization, explainability, and application development rather than provide clinical healthcare services.
