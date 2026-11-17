"""
RECORD CHECK  -  my version
===========================

Name  : jay narolkar
Lane  :  AI 
Date  : 07/11/2026

Run it:   python template.py


"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("it_records.csv")


df["percent"] = (df["used_gb"] / df["total_gb"]) * 100


df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


print("ALL SERVERS")
print(df)


print("\nSERVERS THAT NEED ATTENTION")
print(df[df["status"] != "OK"])


print("\nCOUNT BY STATUS")
print(df.groupby("status").size())


df.to_csv("it_records_report.csv", index=False)


df["status"].value_counts().plot(kind="bar")
plt.title("Server Storage Status")
plt.xlabel("Status")
plt.ylabel("Number of Servers")
plt.tight_layout()
plt.savefig("it_status_counts.png")
plt.show()
