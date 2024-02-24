n = int(input("Enter length of list:"))
l = []
for i in range(0,n):
 l.append(int(input()))
print(*l,sep=",")
print("Largest of the list", max(l))
