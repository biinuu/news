import pandas as pd
import psycopg2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

df = pd.read_csv(r"C:\Users\binuk\Downloads\news_data.csv")

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df = df[['Date', 'Top1']]