"""
RECORD CHECK  -  my version
===========================

Name  :jay narolkar
Lane  :  AI 
Date  :04/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.


label = input("enter the label")
value = float((input("enter the value")))
limit = float((input("enter the limit")))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value - limit
percent = (value / limit)*100
# 3. Decide a status and store it in a variable called status.
#
if percent >= 100:
    status = " OVER LIMIT"
else:
    status = "OK"


# =================================================================== OUTPUT
# 4. Print the report:

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


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
