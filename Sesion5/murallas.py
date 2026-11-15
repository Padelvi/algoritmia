def es_siempre_x(muralla: tuple[int], x: int) -> bool:
    for elem in muralla:
        if elem != x:
            return False
    return True

def es_buena(muralla: tuple[int], x: int, num_torres: int) -> bool:
    if num_torres == 1:
        if muralla[0] == x:
            return True
        else:
            return False
    else:
        pos_mitad = n//2
        mitades = (muralla[:pos_mitad], muralla[pos_mitad:])
        if es_siempre_x(mitades[0],x):
            return es_buena(mitades[1],x,pos_mitad)
        elif es_siempre_x(mitades[1],x):
            return es_buena(mitades[0],x,pos_mitad)
        else:
            return False
        

for _ in range(int(input())):
    n = int(input())
    muralla = tuple(map(int,input().split()))