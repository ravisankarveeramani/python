a = input("enter the list ").split()

print(a)
b = a
print(b)

for i in a:
    for j in i+1:
        print("j=",j)
        print("i=",i)
