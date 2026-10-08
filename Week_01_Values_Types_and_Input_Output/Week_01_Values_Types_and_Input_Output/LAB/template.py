"""
RECORD CHECK  -  my version
===========================

Name  :jay narolkar
Lane  :  AI
Date  :04/10/2026

Run it:   python template.py

"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("enter hostname: ")     
first = float(input("enter GB used: "))    
second = float(input("enter GB total: "))    


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]

difference = second - first   # 
percent = (first/second)*100       


# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"used     :{first:.2f}")
print(f"total    :{second:.2f}")
print(f"free      : {difference:.2f}")
print(f"percent   :{percent:.2f}%")

# : your report lines go here
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
