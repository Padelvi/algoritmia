from itertools import combinations

for _ in range(int(input())):
    regalos = int(input())
    precios = tuple(sorted(map(int,input().split())))

    diffs = []
    for i in range(regalos//2+1):
        for combi in combinations(precios,i):
            diffs.append(abs(sum(precios)-2*sum(combi)))
        # print(combinaciones)
    print(min(diffs))