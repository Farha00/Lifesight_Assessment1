
# Marketing & Business Performance Dashboard
📌 Project Overview

This project implements an interactive BI dashboard to help e-commerce stakeholders understand the impact of marketing activities on business outcomes. The dashboard allows users to upload marketing and business data and provides key insights through metrics and visualizations.

📂 Datasets

The dashboard works with four CSV files:

Google.csv – Campaign-level marketing data (date, tactic, state, campaign, impressions, clicks, spend, attributed revenue).

Facebook.csv – Campaign-level marketing data (same columns as above).

TikTok.csv – Campaign-level marketing data (same columns as above).

Business.csv – Daily business performance (orders, new orders, new customers, total revenue, gross profit, COGS).

📊 Dashboard Features

KPIs: Total Spend, Total Revenue, Orders, ROAS

Time Series: Spend vs Attributed Revenue Over Time

Channel Performance: Metrics by marketing channel

Campaign Leaderboard: Compare campaigns based on ROAS

Date Filter: Interactive slider to select a custom date range

🛠️ How to Use

Clone the repository:

https://github.com/Farha00/Lifesight_Assessment1.git


Install dependencies:

pip install requirements.txt


Run the dashboard:

streamlit run streamlit_app.py


Upload the four CSV files in the sidebar to view the dashboard.

💡 Notes

The dashboard calculates additional metrics:

CTR (Click-Through Rate) = Clicks / Impressions

CPC (Cost per Click) = Spend / Clicks

ROAS (Return on Ad Spend) = Attributed Revenue / Spend

Make sure the CSV files have a date column for proper date filtering.

⚡ Deployment

The dashboard can be deployed on Streamlit Cloud for public access. Users can upload CSVs directly in the sidebar to interact with the dashboard.
URL : https://lifesightassessment1-f8vjicfamikrqsmbxhwdrp.streamlit.app/
