from bisect import insort

for _ in range(int(input())):
    n = int(input())
    piedras = sorted(map(int,input().split()))

    while n > 1:
        mayor, menor = piedras.pop(), piedras.pop()
        diff = mayor - menor
        if diff > 0:
            insort(piedras, mayor-menor)
            n -= 1
        else:
            n -= 2

    print(piedras[0] if piedras else 0)