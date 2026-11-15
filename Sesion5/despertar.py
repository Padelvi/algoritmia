from math import comb

for _ in range(int(input())):
    n = int(input())
    total = 1

    for largos in range(1,n//2+1):
        total += comb(n-largos,largos)

    print(total)