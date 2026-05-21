import streamlit as st
import pandas as pd
import pg8000
import plotly.express as px

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="News Sentiment Dashboard",
    page_icon="📰",
    layout="wide"
)

st.title("📰 News Sentiment Dashboard")
st.markdown("Real-time news sentiment analysis using AWS Lambda + PostgreSQL")

# ---------------------------------
# DATABASE CONNECTION
# ---------------------------------

conn = pg8000.connect(
    host="news-db1.c01qkasokt8i.us-east-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="News12345",
    port=5432
)

# ---------------------------------
# FETCH DATA
# ---------------------------------

query = """
SELECT *
FROM news_sentiment
ORDER BY created_at DESC
LIMIT 100;
"""

df = pd.read_sql(query, conn)

conn.close()