# 📊 Automated EDA & Insight Generation Engine

An end-to-end analytics platform that automates data cleaning, exploratory data analysis (EDA), customer segmentation, anomaly detection, and business insight generation from raw transactional datasets.

The engine transforms raw retail data into actionable business intelligence through automated visualizations, customer analytics, report generation, and interactive dashboards.

---

## 🚀 Features

### Data Processing
- Automated data loading and validation
- Data cleaning and preprocessing
- Missing value handling
- Duplicate record removal
- Revenue feature engineering

### Exploratory Data Analysis (EDA)
- Dataset profiling and summary statistics
- Revenue distribution analysis
- Customer purchasing behavior analysis
- Country-wise revenue analysis

### Customer Analytics
- RFM (Recency, Frequency, Monetary) feature engineering
- Customer segmentation using K-Means clustering
- VIP customer identification
- Dormant customer detection

### Anomaly Detection
- Isolation Forest-based anomaly detection
- Identification of unusual customer purchasing patterns
- Outlier customer analysis

### Automated Insight Generation
- Revenue concentration analysis
- Country-level business insights
- Customer segment analysis
- Pareto (80/20) revenue analysis
- Automated business recommendations

### Reporting & Dashboard
- HTML report generation
- JSON metrics export
- Interactive Streamlit dashboard
- Downloadable analytics outputs

---

## 🏗️ Project Architecture

```text
Raw Dataset
      │
      ▼
Data Loading
      │
      ▼
Data Cleaning
      │
      ▼
EDA Profiling
      │
      ▼
Feature Engineering
      │
      ▼
RFM Segmentation
      │
      ▼
K-Means Clustering
      │
      ▼
Anomaly Detection
      │
      ▼
Insight Generation
      │
      ├────────► HTML Report
      │
      ├────────► JSON Metrics
      │
      ▼
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| File Processing | OpenPyXL |
| Reporting | HTML, JSON |

---

## 📂 Project Structure

```text
Automated-EDA-Engine/
│
├── data/
│
├── reports/
│
├── screenshots/
│
├── src/
│   ├── loader.py
│   ├── cleaner.py
│   ├── profiler.py
│   ├── visualizer.py
│   ├── segmenter.py
│   ├── anomaly_detector.py
│   ├── insight_generator.py
│   ├── report_builder.py
│   ├── metrics_exporter.py
│   └── pipeline.py
│
├── visualizations/
│
├── app.py
├── dashboard.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📈 Analytics Modules

### 1. Customer Segmentation

Customer segmentation is performed using:

- Recency (Last Purchase Date)
- Frequency (Number of Purchases)
- Monetary Value (Total Spending)

The engineered RFM features are clustered using K-Means to identify:

- VIP Customers
- High-Value Customers
- Regular Customers
- Dormant Customers

---

### 2. Anomaly Detection

Isolation Forest is used to identify customers with unusual purchasing behavior.

Examples include:

- Exceptionally high spenders
- Unusual purchasing frequency
- Potential business outliers

---

### 3. Business Insight Engine

The engine automatically generates business-focused insights such as:

- Revenue contribution by country
- VIP customer distribution
- Dormant customer percentage
- Top customer revenue concentration
- Pareto (80/20) analysis
- Anomaly summaries

Example output:

```text
• Total revenue generated: $8,911,407.90

• United Kingdom contributes 91.8% of total revenue.

• Cluster 2 represents 13.4% of customers and contains the highest-value buyers.

• Cluster 0 represents 31.2% of customers and shows dormant purchasing behavior.

• Top 20% of customers generate 78.6% of total revenue.

• 10 anomalous customers were detected.
```

---

## 📊 Dashboard Preview

### Key Metrics
- Total Revenue
- Top Revenue Country
- Anomaly Count

### Business Insights
- Automated insight generation
- Segment-level analysis
- Revenue concentration metrics

### Visualizations
- Revenue by Country
- Top Customers
- Revenue Distribution

### Data Preview
- Cleaned dataset inspection
- Customer analytics outputs

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd Automated-EDA-Engine
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Run Backend Pipeline

```bash
python app.py
```

### Launch Dashboard

```bash
streamlit run dashboard.py
```

---

## 📄 Outputs Generated

### Visualizations

```text
visualizations/
├── revenue_by_country.png
├── top_customers.png
└── revenue_distribution.png
```

### Reports

```text
reports/
├── eda_report.html
└── insights.json
```

---

## 📌 Dataset

This project was developed using the Online Retail dataset from the UCI Machine Learning Repository.

Dataset Characteristics:

- Retail transaction records
- ~540,000 transactions
- Customer-level purchase history
- Multi-country sales data

---

## 🎯 Key Outcomes

- Automated end-to-end EDA workflow
- Customer segmentation using RFM analysis
- Unsupervised anomaly detection
- Automated business insight generation
- Interactive analytics dashboard
- AI-ready structured metrics export

---

## 🔮 Future Enhancements

- Plotly interactive visualizations
- LLM-powered executive summaries
- PDF report generation
- REST API deployment
- Cloud deployment
- Real-time analytics support

---

## 👨‍💻 Author

Developed as a data analytics and machine learning portfolio project focused on automated insight generation and customer intelligence.
