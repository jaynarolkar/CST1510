"""
RECORD CHECK  -  my version
===========================

Name  :jay niraj narolkar
Lane  :  AI 
Date  : 17/10/2026

Run it:   python template.py
"""




def check_record(value, limit):
    
    difference = value - limit
    percent = (value / limit) * 100 if limit != 0 else 0
    #ca;uculate the diffecrece, percentage and status of a record
     if value > limit:
        status = "Over Limit"
    elif value == limit:
        status = "At Limit"
    else:
        status = "Within Limit"
        
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    formatting and priting the record details
    print(f"Record: {label}")
    print(f"Value: {value} | Limit: {limit}")
    print(f"Difference: {difference:+.2f} | Percentage: {percent:.1f}%")
    print(f"Status: {status}")
    print("-" * 30)

with open("my_notes.txt", "w") as f:
    f.write("R-003,89,100\n")
    f.write("R-004,95,100\n")
    f.write("R-005,90,100\n")

def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            label, value, limit = line.split(",")
            value = float(value)
            limit = float(limit)
            record = {"label": label, "value": value, "limit": limit}
            records.append(record)
    return records

load_records("my_notes.txt" )




over_limit_count = 0

for record in records:
  
    status = check_record(record)
 
    print_report(record, status)
    
    if status == "OVER LIMIT":
        over_limit_count += 1


print(f"\nTotal records OVER LIMIT: {over_limit_count}")



