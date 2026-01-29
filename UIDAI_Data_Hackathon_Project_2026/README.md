# 📊 Aadhaar Enrolment and Update Trends

## A Comparative Analysis of Maharashtra and Mumbai Suburban

**UIDAI Data Hackathon 2026 Project**
**Author:** Riddhi More
**Tools Used:** Microsoft Excel, Power BI
**Data Source:** UIDAI Open Data Portal
**Analysis Period:** July 2025 & September 2025

---

## 📌 Project Overview

Aadhaar serves as a foundational digital identity system in India, supporting access to government services, welfare schemes, and financial inclusion. Understanding enrolment and update patterns is essential to assess administrative demand and service accessibility.

This project performs a **comparative analysis of Aadhaar enrolment, demographic updates, and biometric updates** across **Maharashtra (state-level)** and **Mumbai Suburban (urban district)** to evaluate regional service demand and operational pressure during a high-activity period.

---

## 🎯 Objectives

* Analyze Aadhaar enrolment, demographic update, and biometric update trends
* Compare service demand between a state-level region and a dense urban district
* Measure administrative pressure using a derived KPI
* Generate data-driven insights to support region-specific service planning

---

## 🗂️ Dataset Description

* **Datasets Used (3):**

  * Aadhaar Enrolment Data
  * Aadhaar Demographic Update Data
  * Aadhaar Biometric Update Data
* **Geographical Coverage:** Maharashtra, Mumbai Suburban
* **Time Granularity:** Daily (raw), Monthly (post-aggregation)
* **Age Groups Covered (3):** 0–5 years, 5–17 years, 18+ years
* **Format:** CSV files from UIDAI Open Data Portal

---

## ⚙️ Methodology

### 1️⃣ Data Preparation

* Cleaned and standardized raw CSV datasets
* Converted daily data into monthly aggregates
* Consolidated datasets at region level

### 2️⃣ Time Window Selection

* Selected **July 2025 and September 2025** to ensure temporal consistency across enrolment and update services
* Avoided analytical bias caused by partial or non-overlapping service activity

### 3️⃣ Key Metrics (KPIs)

* **Total Enrolments**
* **Total Demographic Updates**
* **Total Biometric Updates**
* **Update Pressure Ratio**

**Formula:**

```
Update Pressure Ratio = (Demographic Updates + Biometric Updates) / Enrolments
```

---

## 📈 Data Analysis & Visualizations

The analysis includes **7 Power BI visualizations**:

1. **Aadhaar Enrolment Trends** – Line chart (Maharashtra vs Mumbai Suburban)
2. **Demographic Update Activity** – Line chart comparison
3. **Biometric Update Activity** – Line chart comparison
4. **Combined Update Activity** – Clustered bar chart (Demographic + Biometric updates)
5. **Update Pressure Ratio Analysis** – Line chart
6. **Enrolment vs Update Pressure** – Combo chart (dual-axis)
7. **Service Load Composition** – Stacked column chart (updates vs enrolment)

---

## 🔍 Key Insights

* Maharashtra records **higher absolute enrolment volumes** due to its larger population base
* Mumbai Suburban shows **higher demographic and biometric update intensity relative to enrolment**
* **Update Pressure Ratio** is consistently higher in Mumbai Suburban, indicating greater administrative load
* Urban Aadhaar service demand is **maintenance-driven**, while state-level demand remains **expansion-focused**
* Excluding partial-period data improved the reliability of comparative insights

---

## 📊 Analytics Type

**Descriptive & Diagnostic Analytics**
The project analyzes historical data to identify trends, regional differences, and drivers of administrative pressure.

---

## 🧠 Conclusion

This study highlights distinct Aadhaar service utilization patterns across regions. While Maharashtra continues to expand enrolment coverage, Mumbai Suburban reflects a mature Aadhaar ecosystem with higher identity maintenance demand. These insights emphasize the need for region-specific Aadhaar service planning.

---

## ✅ Recommendations

* Strengthen Aadhaar update infrastructure and staffing in urban regions
* Maintain enrolment outreach while scaling update services at the state level
* Monitor **Update Pressure Ratio** periodically to detect emerging service bottlenecks
* Extend similar analysis to additional districts for national-level planning

---

## 📂 Repository Structure

```
→ Raw & cleaned UIDAI datasets  
→ Power BI (.pbix) dashboard file  
→ Detailed analysis report (PDF)  
→ Project documentation
→ README.md    
```

---

## 📎 Keywords

UIDAI • Aadhaar Analytics • Power BI • Excel • KPI Reporting • Descriptive Analytics • Diagnostic Analytics • Public Sector Data • Data Visualization • Hackathon Project

---

⭐ *This project was developed as part of the UIDAI Data Hackathon 2026.*
