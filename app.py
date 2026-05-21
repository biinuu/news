import streamlit as st
import pandas as pd
import psycopg2

st.title("📰 News Sentiment Dashboard")

conn = psycopg2.connect(
    database="newsapi",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)

query = "SELECT * FROM news_sentiment ORDER BY created_at DESC"

df = pd.read_sql(query, conn)

conn.close()

# auto refresh
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=300000, key="refresh")
# metrics
positive = len(df[df['sentiment_label'] == 'Positive'])
negative = len(df[df['sentiment_label'] == 'Negative'])

st.metric("Positive News", positive)
st.metric("Negative News", negative)

# charts
st.bar_chart(df['sentiment_label'].value_counts())

# table
st.dataframe(df)