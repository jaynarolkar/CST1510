"""
RECORD CHECK  -  my version
===========================

Name  :jay niraj narolkar
Lane  :  AI 
Date  :10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def status_of(percent):
    """Returns the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Returns the difference and percentage of the limit used."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Prints a report for a single record."""
    print("Label:", label)
    print("Value:", value)
    print("Limit:", limit)
    print("Difference:", difference)
    print("Percentage:", percent)
    print("Status:", status)
    print("--------------------")




label = input("Enter the label: ")      
value = float(input("Enter the value: "))     
limit = float(input("Enter the limit: "))     



difference = value - limit
percent = (value / limit) * 100
status = status_of(percent)



print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here
print(f"  Value:      {value:>10.2f}")
print(f"  Limit:      {limit:>10.2f}")
print(f"  Difference: {difference:>10.2f}")
print(f"  Percent:    {percent:>9.2f}%")
print(f"  Status:     {status:>10}")
print("=" * 34)


