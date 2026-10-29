a = int(input("enter the number "))

b = int(input("enter the number2 "))

op = input("enter the operator ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
else:
    print("enter the correct operator + - * / ")

print("the value is  ",result)

