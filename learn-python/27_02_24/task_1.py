s = input()
vowels_count = 0
non_vowels_count = 0
vowels = "AEIOUaeiou"
for x in s:
 if x in vowels:
  vowels_count+=1
 else:
  non_vowels_count+=1
print("Vowels count:",vowels_count,"\nNon vowels count:",non_vowels_count)
