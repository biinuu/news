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

sia = SentimentIntensityAnalyzer()

conn = psycopg2.connect(
    database="newsapi",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)

cur = conn.cursor()