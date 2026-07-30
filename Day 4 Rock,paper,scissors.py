import random      # Import random module to let the computer choose randomly

# Rock hand image in variable
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper hand image
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Scissors hand image
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List containing the names of the three choices string to take choice for bot
choices = ['rock', 'paper', 'scissors']

# Computer randomly selects one choice from the list
bot_choice = random.choice(choices)

# Take input from the user and convert it to lowercase
user_choice = input("Enter your choice 'rock', 'paper' or 'scissors' : ").lower()

# Display the user's choice
print("\nYou chose:", user_choice)

# Check what the user selected and print the corresponding image
if user_choice == "rock":
    print(rock)          # Print rock image variable call
elif user_choice == "paper":
    print(paper)         # Print paper image
elif user_choice == "scissors":
    print(scissors)      # Print scissors image

# Display the computer's choice
print("Computer chose:", bot_choice)

# Check what the computer selected and print the corresponding image
if bot_choice == "rock":
    print(rock)          # Print rock image
elif bot_choice == "paper":
    print(paper)         # Print paper image
elif bot_choice == "scissors":
    print(scissors)      # Print scissors image

# Compare the user's choice and computer's choice to decide the winner

if user_choice == "rock" and bot_choice == "paper":
    print("Computer Wins")

elif user_choice == "paper" and bot_choice == "rock":
    print("You Win")

elif user_choice == "paper" and bot_choice == "scissors":
    print("Computer Wins")

elif user_choice == "scissors" and bot_choice == "paper":
    print("You Win")

elif user_choice == "scissors" and bot_choice == "rock":
    print("Computer Wins")

elif user_choice == "rock" and bot_choice == "scissors":
    print("You Win")

# If none of the above conditions are true,
# then both the user and computer selected the same option
else:
    print("It's a Draw")