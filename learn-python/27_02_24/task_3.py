a= int(input())
b = int(input())
c = int(input())
if a>b:
 if a>c:
  print(f"{a} is largest among {b} and {c}")
 else:
  print(f"{c} is largest among {b} and {a}")
elif b>c:
 print(f"{b} is largest among {c} and {a}")
else:
 print(f"{c} is largest among {b} and {a}")
