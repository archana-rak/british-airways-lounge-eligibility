# British Airways Lounge Eligibility Project

## Overview
This project estimates lounge eligibility percentages for British Airways passengers
across different regions and times of the day. The analysis is divided into three tiers:
- **Tier 1:** Concorde Room (highest luxury)
- **Tier 2:** First Lounge
- **Tier 3:** Club Lounge

The estimations are based on baseline eligibility percentages for each region
and adjusted for the time of day.

---

## Business Goal
- Predict the actual value of prospective properties.
- Enable management to strategically invest in areas that maximize returns.
- Understand pricing dynamics and passenger segmentation in a new market.

---

## Dataset
The dataset used for this project is:  
[`British_Airways_Lounge_Eligibility.xlsx`](./British_Airways_Lounge_Eligibility.xlsx)

---

## Methodology
1. **Data Preprocessing**
   - Handle missing values (if any)
   - Encode categorical variables
   - Scale features as required

2. **Model Building**
   - **Tier eligibility model:** Apply baseline percentages for each region
   - **Time-of-day adjustments:** Early Morning, Mid-Day, Evening
   - **Automation:** Calculations done in Python

3. **Model Evaluation**
   - Create structured Excel output showing estimated percentages per tier and region

---

## Key Features
- Tier 1: Concorde Room
- Tier 2: First Lounge
- Tier 3: Club Lounge
- Regions: Europe, North America, Middle East, Asia-Pacific, Africa
- Time of Day: Early Morning, Mid-Day, Evening

---

## Tools & Libraries
- Python (`pandas`)
- Excel (for output)
- Optional: Jupyter Notebook for interactive analysis
