s = input()
u=0
l=0
for x in s:
 if x.isupper():
  u+=1
 elif x.islower():
  l+=1
print(f"{s} contains {u} upper case characters and {l} lower case characters")
