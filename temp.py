import psycopg2

conn = psycopg2.connect(
    host="news-db1.c01qkasokt8i.us-east-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="News12345",
    port="5432",
    sslmode="require"
)

cur = conn.cursor()

cur.execute("SELECT * FROM news_sentiment LIMIT 5;")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()