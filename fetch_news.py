import requests
import pandas as pd
import psycopg2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

nltk.download('vader_lexicon')

API_KEY = "your_api_key"

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(url)

data = response.json()

articles = data['articles']

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