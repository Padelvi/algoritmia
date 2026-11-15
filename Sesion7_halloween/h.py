from itertools import combinations

n_casillas, n_pasillos, n_rondas = map(int,input().split())
pasillos = []
for _ in range(n_pasillos):
    pasillos.append(tuple(map(int,input().split())))

laberinto = {node: [] for node in range(1,n_casillas+1)}
for n_orig,n_dest in pasillos:
    laberinto[n_orig].append(n_dest)
    laberinto[n_dest].append(n_orig)


def calcular_caminos(laberinto,orig,dest,fantasmas,caminos_precalculados=None):
    if not caminos_precalculados:
        caminos_precalculados = [[orig]]
    
    caminos_validos = []
    visitados = {orig,*fantasmas}

    def backtrack(laberinto,actual,dest,camino):
        # Caso base: hemos llegado al destino
        if actual == dest:
            caminos_validos.append(camino.copy())
            return

        # Explorar todos los vecinos
        for vecino in laberinto[actual]:

            # Evitar ciclos
            if vecino not in visitados:

                # 1. Elegir: avanzar al vecino
                camino.append(vecino)
                visitados.add(vecino)

                # 2. Explorar: continuar mediante DFS
                backtrack(laberinto,vecino,dest,camino)

                # 3. Deshacer: backtracking
                camino.pop()
                visitados.remove(vecino)

    for camino in caminos_precalculados:
        backtrack(laberinto,orig,dest,camino)

    return caminos_validos

def cortar_camino(camino: list[int], fantasmas: tuple[int]):
    for i,node in enumerate(camino):
        if node in fantasmas:
            del camino[i:]


for _ in range(n_rondas):
    pos_ini = tuple(map(int,input().split()))
    orig, dest, fantasmas =  pos_ini[0], pos_ini[1], pos_ini[2:]

    # Caminos por número de fantasmas
    l = [[] for _ in range(4)]

    pildoras = 0
    while pildoras < 4:
        combs = combinations(fantasmas,4-pildoras)

        posible = False
        for comb in combs:
            caminos_previos = l[pildoras-1].copy()
            for camino in caminos_previos:
                cortar_camino(camino,comb) # type: ignore
            caminos_nuevos = calcular_caminos(laberinto,orig,dest,comb,caminos_previos)

            if caminos_nuevos:
                l[pildoras].extend(caminos_nuevos)
                posible = True
                break

        if posible:
            break

        pildoras += 1

    # print(l)
    print(pildoras)
