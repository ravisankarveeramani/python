a = input("enter the string ")
b = a.lower()
#print(b)
count = 0 
for i in b:
    if i == 'a'or i == 'e' or  i == 'i' or i == 'o' or i == 'u':
        count +=1
print(count)
