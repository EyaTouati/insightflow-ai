#  InsightFlow AI — Smart Business Intelligence System

##  Overview
InsightFlow AI is an end-to-end data analytics platform that transforms raw e-commerce data into actionable business insights using SQL, Python, and Machine Learning.

It simulates a real-world data pipeline used in modern AI-driven startups and consulting firms.

---

##  Objectives
- Clean and structure raw transactional data
- Build KPI dashboards for decision-making
- Segment customers using machine learning
- Generate automated business insights

---

##  Features

###  Business Intelligence
- Revenue analysis
- Orders tracking
- Top-performing countries

###  Customer Analytics
- RFM segmentation (Recency, Frequency, Monetary)
- Customer clustering

###  Machine Learning
- KMeans clustering for customer segmentation

###  Data Engineering
- SQLite database integration
- SQL-based analytics queries

---

##  Machine Learning Model Used

### ✔ KMeans Clustering
Used for unsupervised customer segmentation based on RFM features.

Why KMeans?
- Simple and effective for clustering
- Works well for business segmentation
- Interpretable results for decision-making

---

##  Tech Stack
- Python
- Pandas / NumPy
- Scikit-learn
- SQLite (SQL)
- Streamlit
- Matplotlib

---

## ▶ How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py