from random import randint

t = int(input())
print(t)

for _ in range(t):
    n = randint(15,150)
    q = randint(15,150)
    print(n,q)

    nums = (randint(-50,50) for _ in range(n))
    print(*nums)

    for _ in range(q):
        print(randint(-55,55))