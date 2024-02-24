l = []
n = int(input("Enter length of list:"))
for i in range(0,n):
 l.append(int(input()))
print(*l,sep=",")
average = sum(l)/len(l)
print("Average is",average)
