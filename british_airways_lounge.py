
# British Airways Lounge Eligibility Analysis
# Author: [Your Name]
# Date: 2025-09-05
# Description: This script calculates estimated lounge eligibility percentages
# for different tiers and regions based on the British Airways schedule dataset.

import pandas as pd

# -----------------------------
# Define baseline eligibility %
# -----------------------------
baseline = {
    "Europe": {"Tier1": 0.5, "Tier2": 3.0, "Tier3": 12.0},
    "North America": {"Tier1": 1.5, "Tier2": 6.0, "Tier3": 22.0},
    "Middle East": {"Tier1": 1.0, "Tier2": 5.0, "Tier3": 20.0},
    "Asia-Pacific": {"Tier1": 2.0, "Tier2": 7.0, "Tier3": 24.0},
    "Africa": {"Tier1": 1.0, "Tier2": 5.0, "Tier3": 18.0}
}

# -----------------------------
# Time of Day adjustments
# -----------------------------
time_adjustments = {
    "Early Morning": {"Tier1": 0.2, "Tier2": 0.5, "Tier3": 2.0},
    "Mid-Day": {"Tier1": 0.0, "Tier2": 0.0, "Tier3": 0.0},
    "Evening": {"Tier1": 0.1, "Tier2": 0.3, "Tier3": 1.0}
}

# -----------------------------
# Regions and Times
# -----------------------------
regions = ["Europe", "North America", "Middle East", "Asia-Pacific", "Africa"]
times_of_day = ["Early Morning", "Mid-Day", "Evening"]

# -----------------------------
# Calculate estimated percentages
# -----------------------------
rows = []

for region in regions:
    for time in times_of_day:
        tier1 = baseline[region]["Tier1"] + time_adjustments[time]["Tier1"]
        tier2 = baseline[region]["Tier2"] + time_adjustments[time]["Tier2"]
        tier3 = baseline[region]["Tier3"] + time_adjustments[time]["Tier3"]
        rows.append({
            "Region": region,
            "Time of Day": time,
            "Tier 1 % (Concorde Room)": round(tier1, 2),
            "Tier 2 % (First Lounge)": round(tier2, 2),
            "Tier 3 % (Club Lounge)": round(tier3, 2)
        })

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(rows)

# -----------------------------
# Save to Excel
# -----------------------------
df.to_excel("British_Airways_Lounge_Eligibility.xlsx", index=False)

print("Analysis complete! File saved as 'British_Airways_Lounge_Eligibility.xlsx'.")
