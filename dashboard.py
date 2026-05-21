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

# ---------------------------------
# METRICS
# ---------------------------------

positive_count = len(df[df["sentiment_label"] == "Positive"])
negative_count = len(df[df["sentiment_label"] == "Negative"])
neutral_count = len(df[df["sentiment_label"] == "Neutral"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total News", len(df))
col2.metric("Positive", positive_count)
col3.metric("Negative", negative_count)
col4.metric("Neutral", neutral_count)

# ---------------------------------
# SHOW DATA
# ---------------------------------

st.subheader("Latest News")

st.dataframe(
    df[[
        "news_date",
        "source_name",
        "title",
        "sentiment_score",
        "sentiment_label"
    ]],
    use_container_width=True
)

# ---------------------------------
# SENTIMENT DISTRIBUTION
# ---------------------------------

st.subheader("Sentiment Distribution")

sentiment_count = (
    df["sentiment_label"]
    .value_counts()
    .reset_index()
)

sentiment_count.columns = ["sentiment_label", "count"]

fig_bar = px.bar(
    sentiment_count,
    x="sentiment_label",
    y="count",
    title="Positive vs Negative vs Neutral",
    text_auto=True
)

st.plotly_chart(fig_bar, use_container_width=True)

# ---------------------------------
# PIE CHART
# ---------------------------------

st.subheader("Sentiment Pie Chart")

fig_pie = px.pie(
    sentiment_count,
    names="sentiment_label",
    values="count",
    hole=0.4
)

st.plotly_chart(fig_pie, use_container_width=True)