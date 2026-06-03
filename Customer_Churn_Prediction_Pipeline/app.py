import streamlit as st
import pandas as pd
import joblib

# Load Model and Preprocessor
model = joblib.load("models/random_forest_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

THRESHOLD = 0.65

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🏦 Banking Customer Churn Prediction")

st.write(
    "Predict whether a banking customer is likely to churn."
)

# --------------------------------------------------
# User Inputs
# --------------------------------------------------

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=35
)

tenure = st.slider(
    "Tenure (Years)",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Account Balance",
    min_value=0.0,
    value=50000.0
)

num_products = st.slider(
    "Number of Products",
    min_value=1,
    max_value=4,
    value=2
)

has_card = st.selectbox(
    "Has Credit Card",
    [0, 1]
)

active_member = st.selectbox(
    "Is Active Member",
    [0, 1]
)

salary = st.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=50000.0
)

# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------

balance_salary_ratio = balance / (salary + 1)

products_per_year = num_products / (tenure + 1)

if age <= 30:
    age_group = "Young"
elif age <= 40:
    age_group = "Adult"
elif age <= 50:
    age_group = "MiddleAge"
else:
    age_group = "Senior"

high_value_customer = int(
    balance > 100000 and salary > 100000
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Churn"):

    input_df = pd.DataFrame({
        "CreditScore": [credit_score],
        "Geography": [geography],
        "Gender": [gender],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_products],
        "HasCrCard": [has_card],
        "IsActiveMember": [active_member],
        "EstimatedSalary": [salary],
        "BalanceSalaryRatio": [balance_salary_ratio],
        "ProductsPerYear": [products_per_year],
        "AgeGroup": [age_group],
        "HighValueCustomer": [high_value_customer]
    })

    processed_input = preprocessor.transform(
        input_df
    )

    probability = model.predict_proba(
        processed_input
    )[0][1]

    prediction = int(
        probability >= THRESHOLD
    )

    st.subheader("Prediction Results")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    if prediction == 1:
        st.error(
            "⚠️ High Risk of Churn"
        )
    else:
        st.success(
            "✅ Low Risk of Churn"
        )

    st.write("---")

    st.write("Customer Summary")

    st.dataframe(input_df)