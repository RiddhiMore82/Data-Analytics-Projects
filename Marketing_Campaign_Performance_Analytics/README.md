# 📊 Marketing Campaign Performance Analytics

> Multi-tool analysis project covering SQL

---

## 🗂️ Project Overview

This project performs end-to-end performance analytics on a marketing campaign dataset spanning **6 channels**, **5 cities**, and **multiple audience segments**. The goal is to uncover ROI drivers, detect conversion anomalies, and guide budget reallocation decisions — replicated across four different tech stacks to demonstrate versatility in data analysis and visualization tools.

---

## 📁 Dataset

| Property | Details                          |
|----------|----------------------------------|
| Rows     | 200,000                          |
| Columns  | 16                               |
| File     | `marketing_campaign_dataset.csv` |

**Key columns:** `Campaign_ID`, `Company`, `Campaign_Type`, `Target_Audience`, `Channel_Used`, `Conversion_Rate`, `Acquisition_Cost`, `ROI`, `Location`, `Clicks`, `Impressions`, `Engagement_Score`, `Customer_Segment`, `Date`

---

## 🔍 Key Business Insights

- 📌 Architected a multi-channel ROI analysis across 6 channels and 5 cities — identified **Website** as the top-performing channel at ~5.01 average ROI against a $3B+ total acquisition cost
- 📌 Uncovered a **conversion rate anomaly** — April spike followed by a sharp May drop — enabling data-driven campaign timing corrections across a 12-month trend analysis
- 📌 Segmented performance by audience type and campaign category (Display, Search, Influencer, Social Media) to surface **Email's ~$4.2M CAC** and guide budget reallocation decisions

---

## 🛠️ Tech Stack

This project is implemented across **MySQL** — same dataset, same business questions, different technologies:

| Tool           | Folder  | Status       |
|----------------|---------|--------------|
| 💾 SQL (MySQL) | `/sql`  | ✅ Complete |

---

## 💾 SQL Analysis — Business Questions Solved

| #  | Business Question                                                | 
|----|------------------------------------------------------------------|
| Q1 | Channel-wise average ROI                                         | 
| Q2 | Total acquisition cost by city (> $500M)                         | 
| Q3 | Monthly conversion rate trend — spotting the April/May anomaly   | 
| Q4 | Campaign type × customer segment performance (CAC + ROI)         | 
| Q5 | Top channel per city by ROI using `DENSE_RANK()` window function | 
| Q6 | Month-over-month ROI change with anomaly flagging using `LAG()`  | 

---

## 📊 Power BI — Dashboard Highlights

- Multi-channel ROI dashboard with slicers for channel, city, and campaign type
- 12-month conversion rate trend line with April/May anomaly visible
- Audience segment × campaign category matrix for CAC comparison
- City-level acquisition cost breakdown

---

## 📁 Folder Structure

```
marketing-campaign-analytics/
│
├── dataset/
│   └── marketing_campaign_dataset.csv
│
├── sql/
│   └── marketing_campaign_analysis.sql
│
└── README.md
```

---

## ▶️ How to Use

**SQL**
1. Import `marketing_campaign_dataset.csv` into MySQL
2. Run `sql/marketing_campaign_analysis.sql` in MySQL Workbench

---

## 👩‍💻 Author

**Riddhi More**  
Data Analyst | SQL • Python • Power BI • Tableau • Microsoft Fabric  
📧 riddhi310801@gmail.com  
🔗 [linkedin.com/in/riddhimore3101](https://linkedin.com/in/riddhimore3101)

---

*Part of my multi-domain SQL + BI practice series. Each project will be solved across multiple tools to demonstrate cross-platform analytical skills.*
