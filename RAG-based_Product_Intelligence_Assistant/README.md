# 📊 RAG-Based Product Intelligence Assistant

An AI-powered Product Intelligence Assistant that enables natural language querying over SaaS sales data using Retrieval-Augmented Generation (RAG).

Built using Python, Streamlit, LangChain, TF-IDF retrieval, and OpenAI GPT-4o-mini.

---

# 🚀 Features

* 🔍 Natural language business querying
* 📈 AI-generated business insights
* 🧠 Retrieval-Augmented Generation (RAG)
* 📊 SaaS sales intelligence dashboard
* ⚡ Fast TF-IDF semantic retrieval
* 🤖 OpenAI GPT-4o-mini integration
* 🎨 Interactive Streamlit UI

---

# 🧠 Example Questions

* Which industries generate the highest profits?
* Which products show strong sales performance in EMEA?
* What customer trends can be observed in high-profit sales?
* Which regions demonstrate strong profitability?
* Which customers contribute most to revenue growth?

---

# 🏗️ Project Architecture

```text
User Query
     ↓
TF-IDF Retrieval Engine
     ↓
Relevant Business Records
     ↓
OpenAI GPT-4o-mini
     ↓
AI-Generated Business Insights
     ↓
Streamlit Dashboard
```

---

# 🛠️ Tech Stack

| Component            | Technology             |
| -------------------- | ---------------------- |
| Programming Language | Python                 |
| Frontend             | Streamlit              |
| LLM                  | OpenAI GPT-4o-mini     |
| Retrieval Engine     | TF-IDF                 |
| AI Framework         | LangChain              |
| Dataset              | AWS SaaS Sales Dataset |
| Data Processing      | Pandas                 |
| Similarity Search    | Scikit-learn           |

---

# 📂 Project Structure

```text
RAG-based Product Intelligence Assistant/
│
├── app/
│   └── openai_streamlit_app.py
│
├── data/
│   └── AWS_SaaS_Sales.csv
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
```

---

## 2️⃣ Add OpenAI API Key

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ Do NOT upload your `.env` file to GitHub.

---

## 3️⃣ Run Streamlit App

```bash
streamlit run app/openai_streamlit_app.py
```

---

# 📊 Dataset

This project uses the AWS SaaS Sales Dataset containing:

* Customer data
* Product information
* Regional sales records
* Profit metrics
* Industry segmentation

Dataset size:

* ~10,000 sales records

---

# 🎯 Key Capabilities

## ✅ Intelligent Retrieval

Retrieves the most relevant business records using TF-IDF vectorization and cosine similarity.

## ✅ AI-Powered Insights

Uses GPT-4o-mini to generate concise, professional business insights and strategic recommendations.

## ✅ Interactive Analytics

Enables users to explore sales intelligence through natural language queries.

---

# 📸 Demo

## Example Query

```text
Which industries generate the highest profits?
```

## Example Output

* Executive summary of top-performing industries
* Key business insights
* Strategic recommendations
* Retrieved supporting business records

---

# 🔮 Future Improvements

* 📈 Interactive charts and dashboards
* 📊 KPI analytics cards
* 💬 Conversational chat history
* 📁 CSV upload support
* ☁️ Streamlit Cloud deployment
* 🔍 Advanced hybrid retrieval
* 🧠 Multi-query comparative analysis

---

# 👨‍💻 Author

Developed by Riddhi More

---

# ⭐ If You Like This Project

Give this repository a star ⭐
