l = list(map(int,input().split(",")))
product = 1
for x in l:
 product*=x
print(f"Product of all numbers in list is {product}")
