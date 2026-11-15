def stirling(n: int, k: int) -> int:
    if n==0 and k==0:
        return 1
    elif k==0 or k > n:
        return 0
    else:
        return (n-1)*stirling(n-1,k) + stirling(n-1,k-1)

for _ in range(int(input())):
    n, k = map(int,input().split())
    print(stirling(n,k))