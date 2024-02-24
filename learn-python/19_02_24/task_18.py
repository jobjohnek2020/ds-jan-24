n = input()
vowels = "aeiouAEIOU"
count = 0
for i in n:
 if i in vowels:
  count+=1
print("No of vowels in ", n," is ",count)
