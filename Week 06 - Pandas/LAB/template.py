"""
RECORD CHECK  -  my version
===========================

Name  : jay narolkar
Lane  :  AI 
Date  : 07/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD: read the CSV file
df = pd.read_csv("it_records.csv")

# 2. PROCESS: calculate the percentage of storage used
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# Add a status for each server
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)

# 3. OUTPUT: print the complete table
print("ALL SERVERS")
print(df)

# Show only servers that are not OK
print("\nSERVERS THAT NEED ATTENTION")
print(df[df["status"] != "OK"])

# Count how many servers are in each status
print("\nCOUNT BY STATUS")
print(df.groupby("status").size())

# Save the complete table to a new CSV file
df.to_csv("it_records_report.csv", index=False)

# Make and save a bar chart
df["status"].value_counts().plot(kind="bar")
plt.title("Server Storage Status")
plt.xlabel("Status")
plt.ylabel("Number of Servers")
plt.tight_layout()
plt.savefig("it_status_counts.png")
plt.show()
