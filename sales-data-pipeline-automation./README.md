# 📊 Sales Data Pipeline Automation

An automated pipeline built using **Google Colab**, **Python**, and the **Google Sheets API** to streamline the process of uploading and tracking sales data. This project uses the 
**Adidas Sales dataset** and automatically uploads cleaned sales data to a Google Sheet, along with KPI summaries like **Total Sales by Region** and **Total Sales by Product**.

---

## ✅ Project Highlights

- ⏱️ Automates daily upload of 10K+ sales records from CSV to Google Sheets
- 📍 Tracks performance across multiple product lines and regions
- 📈 Generates KPI summaries for quick business insights
- 💡 Designed for ease of use using Google Colab (no local setup required)
- 🔔 **Future Enhancement**: Real-time alerts when metrics cross defined thresholds

---

## 🧰 Tools & Technologies

| Tool              | Purpose                                 |
|-------------------|------------------------------------------|
| Python (Pandas)   | Data cleaning and KPI calculations       |
| Google Colab      | Cloud-based notebook for running Python  |
| Google Sheets API | Upload data and KPI reports to Sheets    |
| gspread           | Simplified access to Google Sheets API   |
| Adidas Dataset    | Source sales data (CSV from Kaggle)      |

---

## 📁 Folder Structure

automated-sales-tracker/
├── sales-data-pipeline-automation.ipynb # Main Colab notebook
├── AdidasSales.csv # Dataset used (from Kaggle)
├── .gitignore # Hides credentials
└── README.md # Project documentation


> 🔒 `credentials.json` (Google Sheets API key) is not included in the repo for security reasons.

---

## ⚙️ How to Use

1. **Open** the Colab notebook: `Automated_Sales_Tracker.ipynb`
2. **Upload**:
   - `AdidasSales.csv` dataset
   - `credentials.json` (your Google service account file)
3. **Run the notebook** to:
   - Clean and process the data
   - Upload it to Google Sheets
   - Append summary KPIs (Region-wise and Product-wise Total Sales)
4. **Check Google Sheets** to see the full table and summaries auto-generated.

---

## 📊 Example Output

Your Google Sheet will have:
- ✅ Full Adidas sales data (Retailer, Region, Units Sold, etc.)
- 📍 Summary of **Total Sales by Region**
- 📍 Summary of **Total Sales by Product**

---

## 🚀 Future Enhancement

- 🔔 **Real-time alerts** for thresholds like low/high sales or profit dips using email or Slack notifications.

---

## 🙋‍♀️ Author
Riddhi More
Aspiring Data Analyst | MCA Graduate
📍 Mumbai, Maharashtra, India

---

## 📄 License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).
