print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Teasure hunt your mission is to find the teasure ")
choice1=input("you are at a cross road where do you want to go left or right? \n").lower()
if choice1=="left":
    choice2=input("You have come to lake. There is an island in a middle of the lake. \n"
               "Type where you will wait or swim across = \n").lower()
    if choice2 == "wait":
        choice3=input("you have reach unharmed.\n There is a house with 3 door RED, YELLOW, BLUE if you choose"
                      "the right one you will be safe and win the teasure \n if not you will die by the fire or bitten by the snake =\n").lower()
        if choice3 == "yellow":
            print("Great you are safe and won the teasure")
        elif choice3 == "blue":
            print("Sorry, you are killed by snakes")
        else:
            print("Sorry, you are burned by fire")
    else:
        print("you are harmed")

else:
    print("you are hit by care better luck next time")

