import pandas as pd
import psycopg2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

df = pd.read_csv(r"C:\Users\binuk\Downloads\news_data.csv")

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df = df[['Date', 'Top1']]

sia = SentimentIntensityAnalyzer()

df['sentiment_score'] = df['Top1'].apply(
    lambda x: sia.polarity_scores(str(x))['compound']
)

df['sentiment_label'] = df['sentiment_score'].apply(
    lambda x: 1 if x > 0 else 0
)

df.reset_index(inplace=True)

df.rename(columns={
    'index': 'id',
    'Date': 'date',
    'Top1': 'top1'
}, inplace=True)

print(df.head(10))

conn = psycopg2.connect(
    dbname="news_db",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

print("Connected successfully!")

cur.execute("""
DROP TABLE IF EXISTS news_sentiment;

CREATE TABLE news_sentiment (
    id INT,
    date DATE,
    top1 TEXT,
    sentiment_score FLOAT,
    sentiment_label INT
);
""")

conn.commit()