"""
RECORD CHECK  -  my version
===========================

Name  :jay narolkar
Lane  :  AI 
Date  :04/10/2026

Run it:   python template.py

"""



label = input("enter the label")
value = float((input("enter the value")))
limit = float((input("enter the limit")))



difference = value - limit
percent = (value / limit)*100


if percent >= 100:
    status = " OVER LIMIT"
else:
    status = "OK"




print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print("limit: ",limit)
print("value:",value)
print("difference:",difference)
print("percentage:",percent)
print("status:",status)

print("=" * 34)



