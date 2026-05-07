from database import run_query
import pandas as pd

# ================= KPI SQL =================

def total_revenue():
    query = """
    SELECT SUM(Quantity * UnitPrice) AS revenue
    FROM sales
    WHERE Quantity > 0 AND UnitPrice > 0
    """
    return run_query(query)


def total_orders():
    query = "SELECT COUNT(DISTINCT InvoiceNo) AS orders FROM sales"
    return run_query(query)


def top_countries():
    query = """
    SELECT Country, SUM(Quantity * UnitPrice) AS revenue
    FROM sales
    WHERE Quantity > 0 AND UnitPrice > 0
    GROUP BY Country
    ORDER BY revenue DESC
    LIMIT 10
    """
    return run_query(query)


# ================= RFM =================

def build_rfm(df):
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    ref_date = df["InvoiceDate"].max()

    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (ref_date - x.max()).days,
        "InvoiceNo": "count",
        "Revenue": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    return rfm