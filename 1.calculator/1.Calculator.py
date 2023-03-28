import math

print("Hello")
print("You can use this calculator to perform mathematical calculation on one number or between two numbers.")

print("Please select the desired oprator from the options below:")
print("+:sum")
print("-:sub")
print("*:mul")
print("/:div")
print("sin")
print("cos")
print("tan")
print("cot")
print("factorial")

op = (input("Please enter the selected operator: "))

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("Please enter first number:"))
    b = float(input("please enter second number:"))

elif op == "sin" or op == "cos" or op == "tan" or op == "cot":
        a = int(input("Please enter the number:"))

elif op == "sqrt" or op == "factorial":
      a = int(input("enter the number"))

else:
        print("Can`t recognize the selected operator")

if op == "+":
         result = a + b
elif op == "-":
        result = a - b
elif op == "*":
        result = a * b
elif op == "/":
        if b == 0:
            result = "Second number couldn`t be zero"
        else:
            result = a/b


elif op == "sin":
        result = math.sin(a*180/math.pi)
elif op == "cos":
        result = math.cos(a*180/math.pi)
elif op == "tan":
        result = math.tan(a*180/math.pi)
elif op == "cot":
        result = math.cot(a*180/math.pi)


elif op == "sqrt":
        if a < 0:
                result = ("number should be under 0")
        else:
                result = math.sqrt(a)
elif op == "factorial":
        result = math.factorial(a)

if op == "+" or op == "-" or op == "*" or op == "/":
        print(a,op,b,"=",result)
elif op == "sin" or op == "cos" or op == "tan" or op == "cot" or op == "sqrt" or op == "factorial":
        print(a,op,"=",result)



