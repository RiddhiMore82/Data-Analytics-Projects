# 🏦 Banking Customer Churn Prediction Pipeline

## Overview

This project builds an end-to-end machine learning pipeline to predict customer churn in a banking environment. The solution combines automated feature engineering, data preprocessing, model training, threshold optimization, and an interactive Streamlit dashboard to identify customers at risk of leaving the bank.

The objective is to help business and retention teams proactively identify high-risk customers and reduce revenue leakage caused by customer attrition.

---

## Problem Statement

Customer churn is a major challenge for financial institutions. Losing existing customers can result in reduced revenue, lower customer lifetime value, and increased acquisition costs.

This project predicts whether a customer is likely to churn based on demographic, financial, and behavioral attributes.

---

## Dataset

**Banking Customer Churn Dataset**

### Features

* CreditScore
* Geography
* Gender
* Age
* Tenure
* Balance
* NumOfProducts
* HasCrCard
* IsActiveMember
* EstimatedSalary

### Target Variable

* Exited

  * 0 = Customer Retained
  * 1 = Customer Churned

### Dataset Statistics

* Records: 10,000
* Features: 14 original features
* Churn Rate: 20.37%
* Retention Rate: 79.63%

---

## Project Workflow

### 1. Data Audit

* Dataset inspection
* Missing value analysis
* Duplicate record analysis
* Target distribution analysis

### 2. Exploratory Data Analysis (EDA)

Key findings:

* Customers in Germany exhibited higher churn rates.
* Older customers were more likely to churn.
* Active members showed significantly lower churn rates.
* Customers with 2 products demonstrated the highest retention.
* Higher account balances were associated with increased churn risk.

### 3. Feature Engineering

Created business-oriented features:

#### BalanceSalaryRatio

Measures financial intensity by comparing account balance to estimated salary.

#### ProductsPerYear

Captures product adoption velocity relative to customer tenure.

#### AgeGroup

Customer segmentation:

* Young
* Adult
* MiddleAge
* Senior

#### HighValueCustomer

Flags customers with:

* Balance > 100,000
* Estimated Salary > 100,000

---

## Machine Learning Pipeline

### Preprocessing

* One-Hot Encoding for categorical variables
* Standard Scaling for numerical variables
* ColumnTransformer pipeline for reproducibility

### Models Evaluated

#### Logistic Regression (Baseline)

Performance:

* Accuracy: 82.75%
* Precision: 70.0%
* Recall: 26.5%
* F1 Score: 38.5%

#### Random Forest Classifier

Configuration:

```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)
```

Performance:

* Accuracy: 86.5%
* Precision: 84.1%
* Recall: 41.5%
* F1 Score: 55.6%

---

## Threshold Optimization

The default probability threshold (0.50) was adjusted to optimize precision for retention targeting.

### Final Threshold

```python
threshold = 0.65
```

### Final Performance

* Accuracy: 86.5%
* Precision: 90.6%
* Recall: 31.0%

### Business Impact

When the model flags a customer as likely to churn, approximately 91 out of 100 predictions are correct, enabling focused retention campaigns and reducing unnecessary outreach costs.

---

## Streamlit Dashboard

The application allows users to:

* Input customer information
* Generate churn predictions
* View churn probability scores
* Classify customers as:

  * High Risk of Churn
  * Low Risk of Churn

### Run Locally

```bash
streamlit run app.py
```

---

## Project Structure

```text
customer-churn-prediction/
│
├── data/
│   └── churn.csv
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── models/
│   ├── random_forest_model.pkl
│   └── preprocessor.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit

---

## Future Improvements

* Hyperparameter tuning using GridSearchCV
* XGBoost and LightGBM comparison
* SHAP-based explainability
* Automated retraining pipeline
* Cloud deployment using Streamlit Community Cloud or AWS

---

## Results Summary

| Metric    | Final Model |
| --------- | ----------- |
| Accuracy  | 86.5%       |
| Precision | 90.6%       |
| Recall    | 31.0%       |
| F1 Score  | 46.2%       |
| Threshold | 0.65        |

This project demonstrates an end-to-end machine learning workflow from data analysis and feature engineering to model deployment through an interactive Streamlit application.
