import os
import nltk
import json
import requests
import psycopg2
import boto3

nltk.data.path.append("/tmp")

nltk.download("vader_lexicon", download_dir="/tmp")

from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------

API_KEY = "your_api_key"

S3_BUCKET = "news-sentiment-raw-data6"

DB_HOST = "news-db1.c01qkasokt8i.us-east-1.rds.amazonaws.com"

DB_NAME = "postgres"

DB_USER = "postgres"

DB_PASS = "News12345"

# -----------------------------
# AWS S3 CLIENT
# -----------------------------

s3 = boto3.client('s3')

# -----------------------------
# MAIN LAMBDA FUNCTION
# -----------------------------

def lambda_handler(event, context):

        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    response = requests.get(url)

    data = response.json()

    file_name = f"news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=file_name,
        Body=json.dumps(data)
    )

    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port="5432",
        sslmode="require"
    )

    cur = conn.cursor()

    sia = SentimentIntensityAnalyzer()

    for article in data['articles']:

        title = article['title']
        source = article['source']['name']
        published = article['publishedAt']

        score = sia.polarity_scores(title)['compound']

        label = "Positive" if score > 0 else "Negative"

        cur.execute(
            '''
            INSERT INTO news_sentiment
            (
                news_date,
                source_name,
                title,
                sentiment_score,
                sentiment_label
            )
            VALUES (%s, %s, %s, %s, %s)
            ''',
            (
                published,
                source,
                title,
                score,
                label
            )
        )

            conn.commit()

    cur.close()

    conn.close()

    return {
        "statusCode": 200,
        "body": "News inserted successfully!"
    }