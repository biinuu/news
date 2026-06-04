# 📰 Real-Time News Sentiment Analysis Dashboard

## 📌 Project Overview

This project is a **Real-Time News Sentiment Analysis System** built using **AWS Cloud Services, NLP, PostgreSQL, and Streamlit**. The system automatically fetches real-time news headlines, analyzes sentiment using **VADER Sentiment Analysis**, stores processed data in a cloud database, and visualizes results through an interactive dashboard.

The goal of this project is to automate the analysis of news sentiment and classify headlines into **Positive, Negative, and Neutral** categories.

---

## 🚀 Features

* Fetches real-time news headlines using **NewsAPI**
* Performs **sentiment analysis** using **NLTK VADER**
* Stores **raw JSON data** in **Amazon S3**
* Stores processed sentiment data in **PostgreSQL RDS**
* Interactive dashboard using **Streamlit**
* Automated execution using **AWS Lambda**
* Cloud deployment using **Docker + ECR + ECS Fargate**

---

## 🏗️ Project Architecture

```text
NewsAPI
   ↓
AWS Lambda
   ↓
Store Raw JSON in Amazon S3
   ↓
Sentiment Analysis using NLTK VADER
   ↓
Store Processed Data in PostgreSQL RDS
   ↓
Streamlit Dashboard
   ↓
Hosted using ECS Fargate
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### AWS Services

* AWS Lambda
* Amazon S3
* Amazon RDS (PostgreSQL)
* Amazon ECR
* Amazon ECS Fargate
* Amazon EventBridge
* IAM

### Libraries & Frameworks

* Streamlit
* Pandas
* Plotly
* Requests
* NLTK
* psycopg2
* pg8000
* boto3

### Database

* PostgreSQL

---

## 📂 Project Structure

```text
news/
│── lambda/
│   ├── Dockerfile
│   ├── lambda_function.py
│   └── requirements.txt
│
│── dashboard.py
│── fetch_news.py
│── news.py
│── app.py
│── requirements.txt
│── packages.txt
│── Dockerfile.dashboard
│── .gitignore
│── README.md
```

---

## ⚙️ Working Procedure

### Step 1: Fetch News

The system fetches real-time headlines from **NewsAPI** using an API key.

### Step 2: Store Raw Data

Raw JSON response is stored in **Amazon S3** for backup and future analysis.

### Step 3: Sentiment Analysis

News headlines are analyzed using **VADER Sentiment Analyzer** from NLTK.

Sentiment is classified as:

* **Positive** → Score > 0
* **Negative** → Score < 0
* **Neutral** → Score = 0

### Step 4: Database Storage

Processed data is inserted into **PostgreSQL RDS**.

Stored fields include:

* News date
* Source name
* Title
* Sentiment score
* Sentiment label

### Step 5: Dashboard Visualization

The Streamlit dashboard displays:

* Total news count
* Positive news count
* Negative news count
* Neutral news count
* Sentiment distribution charts
* Pie chart visualization
* Top news sources
* Latest news headlines

---

## ☁️ AWS Workflow

```text
EventBridge Trigger
        ↓
AWS Lambda
        ↓
Fetch News from NewsAPI
        ↓
Store JSON in S3
        ↓
Sentiment Analysis
        ↓
Store Results in PostgreSQL RDS
        ↓
Streamlit Dashboard
        ↓
Hosted on ECS Fargate
```

---

## 📊 Dashboard Features

* Real-time sentiment tracking
* Interactive bar charts
* Pie chart visualization
* Top news sources analysis
* Live database updates

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/biinuu/news.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit dashboard:

```bash
streamlit run dashboard.py
```

---

## 🔮 Future Enhancements

* Multi-language sentiment analysis
* Machine learning-based prediction
* Live news streaming
* Advanced analytics dashboard
* Historical sentiment trend analysis

---


