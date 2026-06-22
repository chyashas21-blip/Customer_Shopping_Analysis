# Customer Shopping Behavior Analysis
📌 Overview
This end-to-end data analytics project explores a consumer dataset containing 3,900 transactions across 18 behavioral attributes. The primary objective is to help a leading retail company uncover critical spending patterns, evaluate customer loyalty segments, and pinpoint product preferences. By transforming raw behavioral inputs into structured database segments and interactive dashboard visualizers, this project delivers data-driven marketing strategies to increase subscription rates and optimize promotional campaigns.

📊 Dataset
The dataset tracks demographic factors, behavioral drivers, and final transactional inputs.
- Scope: 3,900 rows × 18 columns
- Key Dimensions: Demographics (Age, Gender), purchase details (Category, Item, Purchase Amount), behavioral metrics (Review Rating, Frequency), and subscription statuses.
- Data Quality State: Initial dataset featured 37 missing observations within the Review Rating attribute which were addressed during processing.

  🛠️ Tools & TechnologiesData Cleaning & Manipulation:
- Data Cleaning & Manipulation: Python (pandas, numpy.
- Database Management: MySQL.
- Interactive Visualization: Power BI.

🔄 Analytical Process Steps
1. Data Preparation & EDA (Python)

- Ingestion: Inspected structures via standard methods (.info(), .describe(), and .shape) to detect anomalies.
- Data Scrubbing: Cleared null profiles and isolated outlier variables to ensure transactional validity.
- Transformation: Normalized text formats, aligned schema header profiles, parsed tracking dates, and generated derived fields for modeling.
- Validation: Verified final null rates and dataset compliance before initializing table imports

2. Relational Schema & Storage (SQL)
- Exported clean objects into structured relational tables.
- Engineered queries to extract target business metrics, evaluating revenue metrics ($233,081 total base) across segmented categories:
  * Gender Revenue Breakdown: Male shoppers accounted for $157,890 across 2,652 buyers, while Female shoppers generated $75,191 across 1,248 buyers.
  * Subscription Patterns: Evaluated spending differences between non-subscribers ($59.87 average) and subscription holders ($59.49 average).
  * Customer Cohorts: Grouped behavior into Loyal (3,116 profiles), Returning (701 profiles), and New (83 profiles) to evaluate retention opportunities.

3. Interactive Visualization (Power BI)
- Engineered a star-schema relationship structure connecting categorical performance metrics.
- Built automated DAX calculations capturing key retail performance indicators: Average Purchase Price ($59.76), Average Rating (3.75), and Subscription Penetration (27% Yes vs. 73% No).
- Constructed interactive layouts featuring dynamic filters for category tracking (Clothing: ~$100K, Accessories: ~$60K, Footwear: ~$30K, Outerwear: ~$10K).

🎨 Dashboard Design
The Power BI environment presents data across three structural focus areas:
1. Executive Overview: High-level cards monitoring gross performance benchmarks, total transaction volume, and global purchase metrics.
2. Demographic Explorers: Comparative visual matrices isolating gender spending dynamics alongside regional age performance groupings.
3. Product & Promo Attribution: Trend charts identifying discount dependence by item type (e.g., Hats at 50% vs. Sweaters at 48.17%) and tracking seasonal ordering peaks around November-December holidays.

📈 Key Insights & Results
- The Retention Challenge: 80% of the customer base qualifies as Loyal , but subscription tiers remain highly underutilized at just 27% adoption.
- Seasonal Fluctuations: Transaction velocity intensifies drastically during the November–December holiday windows, with order frequency averaging every 45 days.
- Category Dominance: Clothing leads company revenue (~$100K), while Outerwear marks the smallest product category (~$10K).

Actionable Business Recommendations:
🚀 Boost Subscriptions: Embed targeted incentive promotions directly into checkout workflows to increase active recurring memberships.
💳 Loyalty Tier Infrastructure: Implement structured point-based incentive tiers targeting the 701 Returning customers to convert them into Loyal tiers.
🎯 Targeted Marketing Distributions: Deploy dedicated marketing allocations toward high-value Young Adult segments and express-shipping historical users.



