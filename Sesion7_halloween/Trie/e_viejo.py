n = int(input())

runas = []
for _ in range(n):
    runas.append(input())

def todos_distintos(pos, let, actual, probar = runas):
    result = set()
    for candidata in runas:
        if candidata == actual:
            continue
        try:
            # print(candidata[pos])
            if candidata[pos] == let:
                result.add(candidata)
        except IndexError:
            continue
    return result

for runa in runas:
    probar = set(runas)
    for i, letra in enumerate(runa):
        # print(i, letra,runa)
        distintos = todos_distintos(i, letra, runa, probar)
        if not distintos:
            print(i+1)
            # encontrado = True
            break
        probar = distintos

    else:
        # encontrado = False
        print(len(runa))
    # print("AAA")