from bisect import bisect_left

for _ in range(int(input())):
    n_horas, n_djs = map(int,input().split())
    aceptaciones = list(map(int,input().split()))
    repets = list(map(int,input().split()))
    tiempos = list(map(int,input().split()))

    tiempos.sort()

    for i in range(tiempos[-1]):
        for a, r in zip(aceptaciones, repets):
            