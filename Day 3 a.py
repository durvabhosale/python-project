'''height=int(input("enter your height:"))
if height>=120 :
    print("your are eligible for your rollercoster ride")
else:
    print("your are not eligible for your rollercoster ride")'''

'''n=int(input("enter your your marks in maths:"))
m=int(input("enter your your marks in english:"))
if n>80 :
    if m>80:
     print("you are good at every thing")
    else:
        print("you are good at maths")
if m>=80 :
    print("you are good at english")'''


print("welcome to the rollercoster ride")
bill=0
height=int(input("enter your height:"))

if height>=120 :
    age=int(input("enter your age:"))
    if age<=12:
        print("please pay $5")
        bill=5
    if age<=18:
        print("please pay $10")
        bill=10
    else :
        print("please pay $15")
        bill=15
else:
    print("you cannot ride rollercoster ride")

photo=input("do you want to take photo?(y/n):")
if photo=="y":
    bill=bill+3
print(bill)
