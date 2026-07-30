import random
print(random.random())
print(random.uniform(10,12))
print(random.randint(10,30))
print(random.sample(range(10,30),2))
print(random.choice(range(10,30)))
a="heads"
b="tails"
print(random.choice([a,b]))

toss= random.randint(1,2)
if toss==1:
    print(a)
else:
    print(b)

friends=["amruta","kunal","rohan","motiram","durva"]
print(random.choice(friends))

frn=random.choice(friends)
print(frn)