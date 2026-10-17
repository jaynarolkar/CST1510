"""
RECORD CHECK  -  my version
===========================

Name  :jay niraj narolkar
Lane  :  AI 
Date  : 17/10/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.


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

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
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


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
over_limit_count = 0

# Loop over each record in the list
for record in records:
    # Call check_record to determine the status
    status = check_record(record)
    
    # Call print_report to display the record's details
    print_report(record, status)
    
    # Keep a running count of "OVER LIMIT" statuses
    if status == "OVER LIMIT":
        over_limit_count += 1

# Print the final count once after the loop finishes
print(f"\nTotal records OVER LIMIT: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
