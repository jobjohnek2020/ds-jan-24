n = int(input())
sqrt = int(n**(1/2))
flag = True
while(sqrt>=2):
 if((n% sqrt)== 0):
  flag = False
  break
 else:
  sqrt-=1
if(flag):
 print(n,"is prime")
else:
 print(n, "is not prime")
