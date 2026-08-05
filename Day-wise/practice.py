import numbers

for n in range(1,101):
    if n<=1:
        print(n)
    else:
        for i in range(2,n):
            if n%i==0:
                print(n)
                break
        else:
            print("prime numbers")

str1=input("enter a string")
rev=""
for ch in str1:
    rev=ch+rev
print(rev)