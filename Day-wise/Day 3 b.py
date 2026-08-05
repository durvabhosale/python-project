print("welcome to dominos")
amt1=0
print("we are exicted to serve you \n ")

print("1.margita pizza  \n" "2.onion pizza  \n""3.chicken pizza \n""4.tandoori pizza \n")
pizza_type=int(input("please which pizza would you like to order :"))

if pizza_type == 1:
    amt1 = 110
    print("Your pizza is: Margherita Pizza")
elif pizza_type == 2:
    amt1 = 180
    print("Your pizza is: Onion Pizza")
elif pizza_type == 3:
    amt1 = 230
    print("Your pizza is: Chicken Pizza")
elif pizza_type == 4:
    amt1 = 250
    print("Your pizza is: Tandoori Pizza")
else:
    print("Pizza is not available")


print("1.small  ")
print("2.medium (+20) ")
print("3.large (+35) ")
size=int(input("choose the size :"))

if size == 1:
    pass
elif size == 2:
    amt1 = amt1 + 20
elif size == 3:
    amt1 = amt1 + 35
else:
    print("The size is not available")


cheese = input("Do you want Cheese? (y/n): ")
if cheese == "y":
    amt1 += 40

corn = input("Do you want Corn? (y/n): ")
if corn == "y":
    amt1 += 30

mushroom = input("Do you want Mushroom? (y/n): ")
if mushroom == "y":
    amt1 += 50

print("Total Bill =", amt1)








