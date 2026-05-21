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