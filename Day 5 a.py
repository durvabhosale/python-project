'''Stud_marks=[20,44,52,55,90,78,42,36,88,96,85,34,72,94,99,49,50]
prev=0
for marks in Stud_marks:
    if marks >=prev:
        prev = marks
print(prev)

sum=0
for i in range(1,101):
    sum=sum+i
print(sum)


for num in range(1,101):
    if num%3 == 0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    elif num%3 and num%5==0:
        print("fizzbuzz")
    else:
        print(num)

#check enter prime number
n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#check 1 to 100 prime number
for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)'''
#prime number

for n in range(1,101):
    if n <=1:
        print(n)
    else:
        for i in range(2,n):
            if n%i==0:
                print(n)
                break
        else:
            print(n,"is prime number")

