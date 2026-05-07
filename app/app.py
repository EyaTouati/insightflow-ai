import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from database import create_database
from analysis import total_revenue, total_orders, top_countries, build_rfm
from insights import generate_insights

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="InsightFlow AI",
    page_icon="",
    layout="wide"
)

# =========================
# MODERN UI STYLE
# =========================
st.markdown("""
<style>

body {
    background-color: #0E1117;
    color: #EAEAEA;
}

/* TITRE */
h1 {
    color: #4DB6FF;
    font-weight: 700;
}

/* KPI CARDS */
[data-testid="metric-container"] {
    background-color: #1C1F26;
    border: 1px solid #2A2F3A;
    padding: 20px;
    border-radius: 12px;
}

/* SUBHEADERS */
h2, h3 {
    color: #FFFFFF;
}

/* TABLE */
.css-1d391kg {
    background-color: #1C1F26;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.title("InsightFlow AI Dashboard")
st.caption("AI-powered Business Intelligence Platform")

# =========================
# INIT DB
# =========================
create_database()

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("data/online_retail.csv", encoding="ISO-8859-1")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df = df.dropna(subset=["CustomerID"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# =========================
# KPI SECTION (MODERN CARDS)
# =========================
st.subheader("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    " Total Revenue",
    f"{total_revenue()['revenue'][0]:,.0f} £"
)

col2.metric(
    " Total Orders",
    int(total_orders()['orders'][0])
)

col3.metric(
    "Customers",
    df["CustomerID"].nunique()
)

st.divider()

# =========================
# TOP COUNTRIES
# =========================
st.subheader("Revenue by Country")

st.bar_chart(top_countries().set_index("Country"))

st.divider()

# =========================
# RFM SEGMENTATION
# =========================
st.subheader("Customer Segmentation (AI Clustering)")

rfm = build_rfm(df)

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

st.dataframe(rfm.head(), use_container_width=True)

st.bar_chart(rfm["Cluster"].value_counts())

st.divider()

# =========================
# INSIGHTS SECTION
# =========================
st.subheader(" AI Business Insights")

insights = generate_insights(df, rfm)

for i in insights:
    st.markdown(f"🔹 {i}")