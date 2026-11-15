from heapq import heapify, heappop, heappush

for _ in range(int(input())):
    n = int(input())
    piedras = list(map(lambda x: -int(x),input().split()))
    heapify(piedras)

    while n > 1:
        mayor, menor = heappop(piedras), heappop(piedras)
        diff = mayor - menor
        if diff < 0:
            heappush(piedras,diff)
            n -= 1
        else:
            n -= 2

    print(-piedras[0] if piedras else 0)