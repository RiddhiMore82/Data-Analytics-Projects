# 🚗 Uber Trip Data Analysis using SQL

This project contains a series of 40+ structured SQL queries written in MySQL Workbench to analyze real-world Uber trip data. It covers beginner to advanced-level use cases such as trip counts, distance insights, duration-based filtering, time-slot analysis, and more.

---

## 📌 Objective:

To extract meaningful insights from Uber trip data using SQL, without relying on visualization tools.

---

## 🔧 Tools Used:

- **MySQL Workbench**
- **Uber Trip Dataset** (with fields like `Start_Date`, `End_Date`, `Category`, `Start`, `Stop`, `Miles`, `Purpose`)

---

## 📂 File Structure:

uber-sql-analysis/
│
├── uber_trip_analysis.sql # All queries grouped by difficulty level
├── uber_dataset.xlsx
├── uber_dataset.csv
└── README.md

---

## 🔍 Key SQL Concepts Used:

- Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`)
- Grouping and Filtering (`GROUP BY`, `WHERE`, `HAVING`, `DISTINCT`)
- Date & Time Functions (`MONTH()`, `DAYNAME()`, `TIMESTAMPDIFF()`, `STR_TO_DATE()`)
- Logical Conditions (`CASE`, `BETWEEN`, `IN`)
- Sorting & Ranking (`ORDER BY`, `LIMIT`)
- Window Functions (`RANK() OVER`, `SUM() OVER`)
- Subqueries & Views

---

## 🧠 Sample Queries:

```sql
-- Total number of trips
SELECT COUNT(*) FROM UberDataset;

-- Average distance per category
SELECT Category, AVG(Miles) FROM UberDataset GROUP BY Category;

-- Top 5 longest trips
SELECT * FROM UberDataset ORDER BY Miles DESC LIMIT 5;

-- Trips with duration over 1 hour
SELECT *, TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) AS DurationMins
FROM UberDataset
WHERE TIMESTAMPDIFF(MINUTE, Start_Date, End_Date) > 60;

--- 

📈 Insights Extracted:
1. Common trip purposes and categories (Business vs Personal)
2. Most frequent start-stop combinations
3. Monthly and weekday trends in trip volumes
4. Distance and duration-based trip analysis
5. Categorization into Short, Medium, Long trips
6. Time-slot grouping (Morning, Afternoon, Evening, Night)

---

### 📌 How to Use:

1. Save this content in your `uber-sql-analysis/README.md` file.
2. Upload to GitHub with your `.sql` file in the same folder.

---

## 🙋‍♀️ Author

**Riddhi More**  
Aspiring Data Analyst | MCA Graduate    
📍 Mumbai, Maharashtra, India

---

## 📄 License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).

