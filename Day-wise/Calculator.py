def addition_number(a,b):
    return a+b

def subtract_numbers(a,b):
    return a-b

def multiply_numbers(a,b):
    return a*b

def divide_numbers(a,b):
    return a/b

operations={"+":addition_number,
            "-":subtract_numbers,
            "*":multiply_numbers,
            "/":divide_numbers}
looping=True
num1 = int(input("Enter first number: "))
while looping == True:
    for symbol in operations:
        print(symbol)
    choice = input("Enter your choice : ")
    num2 = int(input("Enter second number: "))
    calculation = operations[choice]
    result=calculation(num1,num2)
    print(result)

    num1= result
    looping_over=input("Do you want to continue?(y/n)").lower()
    if looping_over == "n":
        print("Goodbye")
        break;







