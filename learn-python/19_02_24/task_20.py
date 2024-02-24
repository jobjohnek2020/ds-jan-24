year = int(input())
if((year%400 == 0) | ((year%100 != 0) & (year%4 == 0))):
 print("Its a leap year")
else:
 print("Its not a leap year")
