import requests
import pandas as pd
import psycopg2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

nltk.download('vader_lexicon')

API_KEY = "cc46542c42274b18aa5fc8136dab67aa"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = data['articles']

sia = SentimentIntensityAnalyzer()

conn = psycopg2.connect(
    database="newsapi",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

for article in articles:

    title = article['title']
    source = article['source']['name']
    published = article['publishedAt']

    score = sia.polarity_scores(title)['compound']

    label = "Positive" if score > 0 else "Negative"

    cur.execute(
        """
        INSERT INTO news_sentiment
        (news_date, source_name, title, sentiment_score, sentiment_label)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (published, source, title, score, label)
    )

conn.commit()

cur.close()
conn.close()

print("News inserted successfully!")