"""
RECORD CHECK  -  my version
===========================

Name  :jay narolkar 
Lane  :  AI 
Date  : 07/11/2026

Run it:   python template.py


"""


def parse_line(raw_line):
    """Clean one messy server line and return its details in a dictionary."""
    clean_line = raw_line.strip()
    parts = clean_line.split(",", 1)
    hostname = parts[0].strip().lower()

    record = {"hostname": hostname}

    for detail in parts[1].split(","):
        key, value = detail.split("=", 1)
        key = key.strip().lower()
        value = value.strip()
        record[key] = float(value)

    return record


def status_of(record):
    """Return the storage status for one server record."""
    percent = (record["used"] / record["total"]) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


raw_records = []

with open("messy_lines_week7_for_template2.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)


flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, "-", status)

    if status != "OK":
        flagged_count = flagged_count + 1

print("Total records:", len(raw_records))
print("Flagged records:", flagged_count)

