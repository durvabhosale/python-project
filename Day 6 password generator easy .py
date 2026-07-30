import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ''
let=int(input("Enter how may letters you want in your password: "))
num=int(input("Enter how many numbers you want in your password: "))
sym=int(input("Enter how many symbols you want in your password: "))

for char in range(0,let):
    password += random.choice(letters)
for n in range(0,num):
    password += random.choice(numbers)
for s in range(0,sym):
    password += random.choice(symbols)
    #print(password) is a simple way
password_list = list(password)
random.shuffle(password_list)
print("".join(password_list))  #here the password will shuffle 


'''
# using join
print("".join(random.choices(letters, k=let))+"".join(random.choices(numbers,k=num))+"".join(random.choices(symbols,k=sym)))

#using variable
password=0
password += random.choices(letters, k=num)
password += random.choices(numbers, k=num)
password += random.choices(symbols, k=num)

random.shuffle(password)
print("".join(password))'''

