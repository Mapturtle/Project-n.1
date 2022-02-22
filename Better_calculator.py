num1= float(input("enter number: "))
op = input("Enter operator: ")
num2= float(input("enter second number"))
if op == "-":
    result= float(num1) - float(num2)
    print(result)
elif op == "+":
    print(num1+ num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Dumbass")