
logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""




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







>>>>>>> ce2b5cd (Add Calculator.py)
