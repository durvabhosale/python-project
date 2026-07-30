print("Welcome to the Tip Calculator")

billamt = float(input("Enter the total bill amount : $ "))
tip = int(input("Enter the tip percentage (10, 12, or 15): "))

if tip == 10:
    total = billamt + (billamt * 10 / 100)
elif tip == 12:
    total = billamt + (billamt * 12 / 100)
elif tip == 15:
    total = billamt + (billamt * 15 / 100) 
else:
    print("Invalid tip percentage")
    exit()

splitmember = int(input("Enter the number of people to split the bill: "))

splitamt = total / splitmember

print("Each person should pay: $",round(splitamt, 2))

#splitamt= ((billamt/splitmember)+tip)



