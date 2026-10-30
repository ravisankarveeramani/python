import random 

a = random.randint(1,100)
print(a)

b = int(input("enter the number "))
i = 1
while (i>0):
    if(a < b):
        print("too high")
        b = int(input("guess it again "))
        i = 0
    elif(a > b):
        print("too low")
        b = int(input("guess it again "))
        i = 0 
    elif(a == b):
        print("congrats , you got it correct")
        i = -1
    else:
        print("enter the correct value")
    i += 1
