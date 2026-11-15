mensajeros = int(input())
l = list(map(int,input().split()))
l.sort()

grupos = mensajeros // 3

print(sum(l[-2::-2][:grupos]))