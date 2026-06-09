import requests
import pandas as pd
import psycopg2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

response = requests.get(url)

data = response.json()

articles = data['articles']

for article in articles:

    title = article['title']
    source = article['source']['name']
    published = article['publishedAt']

    score = sia.polarity_scores(title)['compound']

    label = "Positive" if score > 0 else "Negative"