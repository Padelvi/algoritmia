def min_diff(regalos: int, precios: tuple, anterior: int = 0):
    if regalos == 0:
        return anterior
    else:
        precio = precios[0]
        nuevo = min(abs(anterior-precio),abs(anterior+precio))
        # print(nuevo)
        return min_diff(regalos-1,precios[1:],nuevo)

for _ in range(int(input())):
    regalos = int(input())
    precios = tuple(sorted(map(int,input().split())))
    print(min_diff(regalos,precios))