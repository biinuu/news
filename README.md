# 📰 Real-Time News Sentiment Analysis Dashboard using AWS, NLP & Streamlit

<p align="center">

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge\&logo=python)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge\&logo=amazonaws)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge\&logo=postgresql)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge\&logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge\&logo=docker)

</p>

---

# 📌 Project Overview

This project is a **Real-Time News Sentiment Analysis Dashboard** that automatically collects live news headlines, performs **sentiment analysis using NLP**, stores the processed results inside a cloud database, and visualizes everything through an interactive dashboard.

The entire system is automated using **AWS Cloud Services**, making the project scalable, cloud-native, and production-ready.

This system helps users understand:

* Whether news sentiment is **positive**, **negative**, or **neutral**
* Which news sources publish the most content
* Real-time sentiment trends
* Headline analytics

Instead of manually reading hundreds of news articles, the system performs sentiment analysis automatically.

---

# 🎯 Project Objective

The primary objective of this project is:

> To build an automated cloud-based system that fetches real-time news, analyzes sentiment using NLP, stores processed data in PostgreSQL, and visualizes results through an interactive Streamlit dashboard.

---

# 👨‍💻 Why This Project Was Built

Every day, thousands of news articles are published.

Reading all news manually to understand public sentiment is:

❌ Time consuming
❌ Difficult to analyze at scale
❌ Not suitable for real-time insights

This project solves that problem by creating an automated pipeline:

```text
Fetch News
      ↓
Analyze Emotion
      ↓
Store Data
      ↓
Visualize Insights
```

The system runs automatically using AWS.

---

# 🌐 Live Project Links

### GitHub Repository

https://github.com/biinuu/news

### Live Streamlit Dashboard

(Current ECS Public IP — may change after task restart)

http://98.93.215.229:8501

---

# 🏗️ Complete Project Architecture

```text
                     ┌─────────────────────┐
                     │      NewsAPI        │
                     │  Real-Time Headlines│
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │    AWS Lambda       │
                     │ Data Processing     │
                     └──────────┬──────────┘
                                │
               ┌────────────────┴──────────────┐
               │                               │
               ▼                               ▼
    ┌──────────────────┐         ┌─────────────────────┐
    │   Amazon S3      │         │ NLP Sentiment       │
    │ Raw JSON Backup  │         │ Analysis (VADER)    │
    └──────────────────┘         └──────────┬──────────┘
                                             │
                                             ▼
                              ┌─────────────────────────┐
                              │ PostgreSQL RDS Database │
                              │ Processed News Storage  │
                              └──────────┬──────────────┘
                                         │
                                         ▼
                              ┌────────────────────────┐
                              │ Streamlit Dashboard    │
                              │ Interactive Analytics  │
                              └──────────┬─────────────┘
                                         │
                                         ▼
                              ┌────────────────────────┐
                              │ ECS Fargate Hosting    │
                              │ Public Dashboard       │
                              └────────────────────────┘
```

---

# 🔄 Project Flowchart

```text
NewsAPI
   ↓
AWS Lambda Triggered
   ↓
Fetch Live Headlines
   ↓
Store Raw JSON in Amazon S3
   ↓
Perform Sentiment Analysis (VADER NLP)
   ↓
Store Processed Results in PostgreSQL RDS
   ↓
Dashboard Fetches Data
   ↓
Streamlit Visualizes Results
   ↓
Hosted on ECS Fargate
   ↓
User Views Dashboard
```

---

# 🧠 Beginner Friendly Explanation

If you do not know coding, think of this project like this:

### Step 1 → Collect News

The system automatically reads live news from the internet.

### Step 2 → Understand Emotion

Using AI/NLP, it checks:

Is this headline:

😊 Positive?
😐 Neutral?
😡 Negative?

### Step 3 → Save Results

The processed data gets stored safely in a cloud database.

### Step 4 → Show Dashboard

Charts and analytics are displayed visually for users.

### Step 5 → Cloud Hosting

The entire dashboard is hosted online using AWS.

This means:

> The system works automatically without manually running code every time.

---

# 🛠️ Technologies Used

## Programming Language

### Python

Python is used as the main programming language because:

* beginner friendly
* strong NLP support
* AWS SDK support
* database connectivity
* dashboard integration

---

## AWS Services Used

| Service        | Purpose                         |
| -------------- | ------------------------------- |
| AWS Lambda     | Automates backend execution     |
| Amazon S3      | Stores raw JSON backup          |
| PostgreSQL RDS | Stores processed sentiment data |
| Amazon ECS     | Hosts Streamlit dashboard       |
| Amazon ECR     | Stores Docker images            |
| EventBridge    | Schedules Lambda execution      |
| IAM            | Provides secure permissions     |

---

# 📂 Project Folder Structure

```text
news/
│
├── dashboard.py
├── app.py
├── fetch_news.py
├── news.py
├── temp.py
│
├── Dockerfile.dashboard
├── requirements.txt
├── packages.txt
│
├── lambda/
│   ├── lambda_function.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

# 📁 File Purpose Explanation

## 1. `fetch_news.py`

### Purpose

Responsible for:

* fetching live news
* performing sentiment analysis
* inserting processed data into database

### Related GitHub Code

https://github.com/biinuu/news/blob/main/fetch_news.py

---

## 2. `dashboard.py`

### Purpose

Creates the main Streamlit dashboard.

Displays:

* metrics
* charts
* latest news
* analytics

### Related GitHub Code

https://github.com/biinuu/news/blob/main/dashboard.py

---

## 3. `app.py`

### Purpose

Contains additional dashboard logic and visualizations.

### Related GitHub Code

https://github.com/biinuu/news/blob/main/app.py

---

## 4. `news.py`

### Purpose

Used for database verification and querying.

### Related GitHub Code

https://github.com/biinuu/news/blob/main/news.py

---

## 5. `temp.py`

### Purpose

Temporary RDS database connection testing.

### Related GitHub Code

https://github.com/biinuu/news/blob/main/temp.py

---

## 6. `lambda/lambda_function.py`

### Purpose

Main AWS Lambda backend logic.

Responsible for:

* fetching news
* storing JSON in S3
* NLP analysis
* inserting into PostgreSQL

### Related GitHub Code

https://github.com/biinuu/news/blob/main/lambda/lambda_function.py

---

## 7. `lambda/Dockerfile`

### Purpose

Creates Docker container for Lambda.

### Related GitHub Code

https://github.com/biinuu/news/blob/main/lambda/Dockerfile

---

## 8. `Dockerfile.dashboard`

### Purpose

Containerizes Streamlit dashboard.

### Related GitHub Code

https://github.com/biinuu/news/blob/main/Dockerfile.dashboard

---

## 9. `requirements.txt`

### Purpose

Contains Python dependencies.

### Related GitHub Code

https://github.com/biinuu/news/blob/main/requirements.txt

---

## 10. `packages.txt`

### Purpose

Contains system packages for deployment.

### Related GitHub Code

https://github.com/biinuu/news/blob/main/packages.txt

# ⚙️ Step-by-Step Project Working Procedure

This section explains **exactly how the system works internally**, step by step, in a beginner-friendly way.

Even if you do not know coding, you should be able to understand how the system operates.

---

# Step 1 — Fetching Real-Time News Data

## What happens?

The project first collects **live news headlines** from the internet.

Instead of manually searching for news, the system automatically fetches news from:

## NewsAPI

Website:

https://newsapi.org

NewsAPI provides:

* live headlines
* news source
* publish date
* metadata

The system sends an API request to:

```text
https://newsapi.org/v2/top-headlines
```

Then NewsAPI returns data in:

## JSON format

Example:

```json
{
"title": "Stock market rises",
"source": {
"name": "BBC"
},
"publishedAt": "2025-06-10"
}
```

---

## Why NewsAPI Was Used?

Because it provides:

✅ Real-time data
✅ Free API access
✅ Structured JSON response
✅ Easy integration with Python

Without NewsAPI:

```text
manual news collection
```

would be required.

---

## Related Code

### News Fetching Logic

https://github.com/biinuu/news/blob/main/fetch_news.py

### Lambda News Fetching

https://github.com/biinuu/news/blob/main/lambda/lambda_function.py

---

# Step 2 — AWS Lambda Automation

## What is Lambda?

AWS Lambda is a:

## Serverless Computing Service

Meaning:

You do not manage servers.

AWS automatically runs your code.

---

## Why Lambda Was Used?

Without Lambda:

You would manually run:

```bash
python fetch_news.py
```

every time.

This is bad because:

❌ manual work
❌ not automated
❌ laptop must stay ON

Lambda solves this.

It automatically executes:

```python
lambda_handler(event, context)
```

which runs:

1. fetch news
2. store raw JSON
3. perform sentiment analysis
4. insert into PostgreSQL

---

## How Lambda Works in This Project

```text
EventBridge Trigger
        ↓
AWS Lambda Starts
        ↓
Fetch News
        ↓
Analyze Sentiment
        ↓
Store in Database
```

---

## Why Lambda Instead of EC2?

Lambda was chosen because:

| Lambda               | EC2                        |
| -------------------- | -------------------------- |
| automatic            | manual                     |
| no server management | server management required |
| pay per execution    | pay continuously           |

Since this project only needs scheduled execution:

## Lambda was better.

---

## Related Code

### Lambda Backend Logic

https://github.com/biinuu/news/blob/main/lambda/lambda_function.py

---

# Step 3 — Amazon S3 Raw Data Storage

## What is S3?

Amazon S3 =

## Simple Storage Service

Used for storing files in cloud.

---

## Why S3 Was Used?

When news is fetched:

Raw JSON data is stored in:

## S3 Bucket

This acts like:

## Backup Storage

Suppose database fails.

Without S3:

```text
all fetched data lost
```

With S3:

```text
raw data backup exists
```

---

## What gets stored?

Example:

```json
{
"articles":[...]
}
```

Entire API response is stored.

---

## How S3 Works

```text
Lambda Fetches News
          ↓
JSON Response Created
          ↓
Saved into S3 Bucket
```

---

## Related Code

### S3 Upload Logic

https://github.com/biinuu/news/blob/main/lambda/lambda_function.py

Look for:

```python
s3.put_object()
```

---

# Step 4 — NLP Sentiment Analysis

## What is NLP?

NLP =

## Natural Language Processing

It helps computers understand human language.

Example:

Human reads:

```text
Economy crashes badly
```

Human instantly knows:

❌ Negative news

Computer cannot understand emotion naturally.

So we use:

## VADER Sentiment Analysis

---

## Why VADER?

VADER is:

### Pre-trained NLP Model

Meaning:

No machine learning training needed.

It already understands sentiment.

---

## How It Works

Headline:

```text
Stock market rises
```

VADER returns:

```text
+0.8
```

Positive.

Headline:

```text
Economy crashes
```

Returns:

```text
-0.7
```

Negative.

---

## Sentiment Rules

| Score | Meaning  |
| ----- | -------- |
| > 0   | Positive |
| < 0   | Negative |
| = 0   | Neutral  |

---

## Why VADER Was Chosen?

Because:

✅ Fast
✅ Beginner friendly
✅ Accurate for text sentiment
✅ No training required

---

## Related Code

### Sentiment Analysis Logic

https://github.com/biinuu/news/blob/main/fetch_news.py

### Lambda NLP Logic

https://github.com/biinuu/news/blob/main/lambda/lambda_function.py

Look for:

```python
SentimentIntensityAnalyzer()
```

and

```python
polarity_scores()
```

---

# Step 5 — PostgreSQL Database Storage

## Why Database Needed?

After sentiment analysis:

Need permanent storage.

Data cannot stay only in RAM.

So project uses:

## PostgreSQL

inside:

## AWS RDS

---

## What is RDS?

RDS =

## Relational Database Service

AWS-managed cloud database.

---

## Why RDS Instead of Local Database?

Local database problem:

❌ only works on laptop
❌ inaccessible online

RDS benefits:

✅ cloud hosted
✅ scalable
✅ accessible anywhere
✅ secure

---

## What Data Gets Stored?

| Column          | Meaning                   |
| --------------- | ------------------------- |
| news_date       | publish date              |
| source_name     | news source               |
| title           | headline                  |
| sentiment_score | NLP score                 |
| sentiment_label | positive/negative/neutral |

---

## Database Workflow

```text
News Headline
       ↓
Sentiment Score
       ↓
Insert into PostgreSQL
```

---

## Related Code

### Database Insert Logic

https://github.com/biinuu/news/blob/main/fetch_news.py

### Lambda DB Logic

https://github.com/biinuu/news/blob/main/lambda/lambda_function.py

### Query Testing

https://github.com/biinuu/news/blob/main/news.py

### RDS Testing

https://github.com/biinuu/news/blob/main/temp.py

---

# Step 6 — Streamlit Dashboard

## Why Dashboard Needed?

Raw database data is hard to understand.

Users prefer:

📊 Charts
📈 Visuals
📋 Tables

So we built:

## Streamlit Dashboard

---

## What Dashboard Shows

### Metrics

* total news
* positive news
* negative news
* neutral news

### Charts

* bar chart
* pie chart
* sentiment distribution

### Data Table

Latest news headlines.

---

## Why Streamlit?

Because:

✅ Python based
✅ Easy UI creation
✅ Fast dashboard development

---

## Related Code

### Dashboard Logic

https://github.com/biinuu/news/blob/main/dashboard.py

### Extra Visualization

https://github.com/biinuu/news/blob/main/app.py


# ☁️ AWS Services Deep Explanation

This section explains **why each AWS service was used**, what problem it solves, and how it works inside this project.

---

# Step 7 — Docker Containerization

## What is Docker?

Docker is a:

## Containerization Tool

It packages:

* Python code
* libraries
* dependencies
* runtime environment

inside one portable container.

Think of Docker like:

## A portable box containing your project

So it works exactly the same everywhere.

---

## Why Docker Was Used?

Problem:

AWS Lambda and ECS require dependencies.

Libraries such as:

```text id="g8x2wr"
nltk
psycopg2
pg8000
boto3
```

sometimes fail during deployment.

Docker solves this by packaging everything together.

Without Docker:

❌ dependency conflicts
❌ deployment failures
❌ inconsistent environment

With Docker:

✅ same environment everywhere
✅ easy deployment
✅ reproducible setup

---

## Docker Workflow

```text id="m7v2pk"
Code
   ↓
Dockerfile
   ↓
Docker Image
   ↓
ECR Storage
   ↓
Lambda / ECS Execution
```

---

## Related Code

### Lambda Dockerfile

https://github.com/biinuu/news/blob/main/lambda/Dockerfile

### Dashboard Dockerfile

https://github.com/biinuu/news/blob/main/Dockerfile.dashboard

### Dependencies

https://github.com/biinuu/news/blob/main/requirements.txt

https://github.com/biinuu/news/blob/main/lambda/requirements.txt

---

# Step 8 — Amazon ECR (Elastic Container Registry)

## What is ECR?

ECR =

## Elastic Container Registry

Purpose:

Store Docker images.

Think:

```text id="x2r9mk"
GitHub for Docker images
```

---

## Why ECR Was Used?

After building Docker image:

Need cloud storage.

AWS services cannot directly run:

```text id="t6m3wr"
Dockerfile
```

They need:

## Docker Image

stored somewhere.

That place is:

## Amazon ECR

---

## Workflow

```text id="h8m2qn"
Docker Build
      ↓
Push Image to ECR
      ↓
ECS/Lambda pulls image
      ↓
Application runs
```

---

## Why ECR Instead of Local Image?

Local image:

❌ only available on laptop

ECR:

✅ cloud accessible
✅ secure
✅ scalable

---

## Related Code

### Lambda Container

https://github.com/biinuu/news/blob/main/lambda/Dockerfile

### Dashboard Container

https://github.com/biinuu/news/blob/main/Dockerfile.dashboard

---

# Step 9 — Amazon ECS (Elastic Container Service)

## What is ECS?

ECS =

## Container Hosting Service

Purpose:

Run Docker containers.

---

## Why ECS Was Used?

The dashboard must stay:

## Online 24/7

Lambda cannot host dashboards continuously.

Lambda only works for:

```text id="d5m8pk"
short execution
```

But Streamlit dashboard requires:

```text id="n9v2ql"
continuous hosting
```

So ECS was used.

---

## Why ECS Instead of EC2?

| ECS                    | EC2                      |
| ---------------------- | ------------------------ |
| no server management   | manual server management |
| scalable               | more maintenance         |
| easy container hosting | more setup               |

ECS Fargate automatically runs containers.

---

## ECS Workflow

```text id="j3v7mk"
Dashboard Code
       ↓
Docker Container
       ↓
Push to ECR
       ↓
ECS pulls image
       ↓
Dashboard hosted online
```

---

## Related Code

### Dashboard Code

https://github.com/biinuu/news/blob/main/dashboard.py

### Dashboard Container

https://github.com/biinuu/news/blob/main/Dockerfile.dashboard

---

# Step 10 — EventBridge Scheduling

## What is EventBridge?

EventBridge is:

## AWS Scheduling Service

Used to automate Lambda execution.

---

## Why EventBridge Was Used?

Without EventBridge:

Need manual execution.

Example:

```bash id="y1m8qp"
python fetch_news.py
```

every time.

Bad approach.

EventBridge automates:

```text id="s8r2pk"
every hour
every day
custom schedule
```

---

## Workflow

```text id="k2m7qn"
EventBridge Trigger
         ↓
Lambda Starts Automatically
         ↓
News Processing Begins
```

---

## Why Needed?

Because project should:

```text id="q9v4mk"
run automatically
```

without human involvement.

---

# Step 11 — IAM (Identity Access Management)

## What is IAM?

IAM controls:

## Permissions

between AWS services.

---

## Why IAM Was Needed?

Lambda needed access to:

* S3
* CloudWatch
* RDS

Without IAM:

```text id="g4r8pk"
Access Denied
```

error happens.

IAM securely allows:

```text id="x5m9wr"
Lambda → S3
Lambda → Logs
```

---

## Example Permission

```text id="b7v2pl"
S3 PutObject
```

Allows Lambda to upload JSON.

---

# 🚀 Full Deployment Guide

This section explains how to rebuild the project from zero.

---

## Step 1 — Clone Repository

```bash id="k9q2mn"
git clone https://github.com/biinuu/news.git
```

Move inside folder:

```bash id="h7r4pk"
cd news
```

---

## Step 2 — Install Dependencies

```bash id="v8m2wr"
pip install -r requirements.txt
```

---

## Step 3 — Create NewsAPI Account

Create API key:

https://newsapi.org

Replace:

```python id="r6m8qp"
API_KEY = "your_api_key"
```

inside:

```text id="x2v9mn"
fetch_news.py
```

---

## Step 4 — Configure PostgreSQL

Create database.

Update credentials.

---

## Step 5 — Run News Fetch

```bash id="m5q8pk"
python fetch_news.py
```

---

## Step 6 — Run Dashboard

```bash id="w4m2ql"
streamlit run dashboard.py
```

---

# 🛠️ Troubleshooting Guide

## Problem: Streamlit Not Opening

### Fix

Check:

```text id="v9r2pk"
port 8501
```

is open in ECS Security Group.

Use:

```text id="n4m8wr"
http://public-ip:8501
```

---

## Problem: Database Connection Error

### Fix

Check:

* RDS endpoint
* username
* password
* port 5432

---

## Problem: Lambda Error

### Fix

Check:

CloudWatch logs.

Verify:

* IAM permission
* Docker image
* dependencies

---

## Problem: ECS Timeout

### Fix

Check:

* running task
* public IP
* security group

---

## Problem: NewsAPI Error

### Fix

Check:

```text id="q8m2pk"
API_KEY
```

validity.

---

# 🎓 Viva / Interview Questions

## Q1. Why did you choose AWS Lambda?

### Answer

Lambda was used to automate backend execution without server management.

---

## Q2. Why ECS instead of EC2?

### Answer

ECS was easier for container hosting and required less server maintenance.

---

## Q3. Why ECR?

### Answer

ECR stores Docker images required for ECS and Lambda deployment.

---

## Q4. Why PostgreSQL?

### Answer

Because structured sentiment data requires relational storage.

---

## Q5. Why S3?

### Answer

S3 stores raw JSON backup before processing.

---

## Q6. Why VADER?

### Answer

VADER provides fast pre-trained sentiment analysis without model training.

---

## Q7. Why Docker?

### Answer

Docker ensures dependency consistency and easier deployment.

---

# 🔮 Future Enhancements

* Machine learning sentiment prediction
* Multi-language support
* Live streaming analytics
* Historical trend analysis
* AI summarization

---

# 👨‍💻 Author

### Binu K V

**MSc Data Analytics Project**

GitHub Repository:

https://github.com/biinuu/news
