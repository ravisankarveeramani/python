a = input("enter the string ")
b = a.lower()
#print(b)
count = 0 
for i in b:
    if i in 'aeiou':
        count +=1
print(count)
