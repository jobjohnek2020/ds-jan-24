n = int(input())
flag = True
sqrt = int(n**(1/2))
for x in range(2,sqrt):
 if((n%x)==0):
  flag = False
  break
if(flag):
 print(f"{n} is prime")
else:
 print(f"{n} is not prime")
