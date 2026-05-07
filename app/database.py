import sqlite3
import pandas as pd
import os

DB_PATH = "database/retail.db"
CSV_PATH = "data/online_retail.csv"


def create_database():
    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_csv(CSV_PATH, encoding="ISO-8859-1")

    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()


def get_connection():
    return sqlite3.connect(DB_PATH)


def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df