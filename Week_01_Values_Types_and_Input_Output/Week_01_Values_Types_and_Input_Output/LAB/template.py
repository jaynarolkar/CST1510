"""
RECORD CHECK  -  my version
===========================

Name  :jay narolkar
Lane  :  AI
Date  :04/10/2026

Run it:   python template.py

"""



label = input("enter hostname: ")     
first = float(input("enter GB used: "))    
second = float(input("enter GB total: "))    



difference = second - first   # 
percent = (first/second)*100       



print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"used     :{first:.2f}")
print(f"total    :{second:.2f}")
print(f"free      : {difference:.2f}")
print(f"percent   :{percent:.2f}%")

print("=" * 34)


