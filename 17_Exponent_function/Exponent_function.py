def power(num_1,num_2):
    result = 1
    for index in range(num_2):
        result = result * num_1
    return result
num1 = int(input("pleasr enter first number"))
num2 = int(input("please enter second number"))
print(power(num1,num2))
