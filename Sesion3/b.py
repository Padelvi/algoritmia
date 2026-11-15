from bisect import bisect_left

def leer_entero():
    linea = input()
    while not linea.strip():      # salta líneas vacías
        linea = input()
    return int(linea)

def leer_lista(n):
    lista = []
    while len(lista) < n:         # si n = 0 no lee ninguna línea
        lista += map(int, input().split())
    return lista

for _ in range(leer_entero()):
    num_billetes = leer_entero()
    billetes = sorted(leer_lista(num_billetes))
    num_precios = leer_entero()
    precios = leer_lista(num_precios)

    for precio in precios:
        if num_billetes == 0:
            print(-1)
            continue
        if billetes[-1] < precio:
            print(-1)
            continue
        i = bisect_left(billetes, precio)
        print(billetes[i] - precio)

    print("---")