num1 = float(input("please enter frist number : "))
operator=input("please enter operator system : ")
num2 =float( input("please enter second number : "))
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("no results")
