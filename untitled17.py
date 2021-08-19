file = open('data1.txt','rt')
data = file.read()
count_digit = 0
upper = 0
lower = 0
for char in data:
    if char.isdigit():
        count_digit += 1
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
print("the digit count is:",count_digit)
print("the uppercase count is:",upper)
print("the lowercase count is:",lower)        
words=data.split()
print("no of words are:",len(words))