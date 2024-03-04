print("Enter lower limit, upper limit and the number to be checked in the range line by line")
l,u,n=int(input()),int(input()),int(input())
if(l<n<u):
 print(f"{n} falls within the range {l} and {u}")
else:
 print(f"{n} not falls within the range {l} and {u}")
