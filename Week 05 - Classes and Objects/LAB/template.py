"""
RECORD CHECK  -  my version
===========================

Name  : jay narolkar
Lane  :  AI 
Date  :24/10/2026

Run it:   python template.py


"""



# your class goes here
class Record:
    """Store a labeled value and its limit."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialize the record's label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit
        if self.value >= self.limit:
            Record.over_limit_count += 1

    def status(self):
        """Return the status based on the value's proportion of its limit."""
        if self.value >= self.limit:
            return "OVER LIMIT"
        if self.value >= self.limit * 0.9:
            return "WARNING"
        return "OK"




records = [Record("Water usage", 95, 100),Record("Energy usage", 110, 100),]

for record in records:
    print(f"{record.label}: {record.status()}")




over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    status = record.status()
    print(f"  Status : {status}")
    if status == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)

print(f"OVER LIMIT records: {over_limit_count}")



