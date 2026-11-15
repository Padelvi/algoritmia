from itertools import combinations

n_casillas, n_pasillos, n_rondas = map(int,input().split())
pasillos = []
for _ in range(n_pasillos):
    pasillos.append(tuple(map(int,input().split())))

laberinto = {node: [] for node in range(1,n_casillas+1)}
for n_orig,n_dest in pasillos:
    laberinto[n_orig].append(n_dest)
    laberinto[n_dest].append(n_orig)


def calcular_caminos(laberinto,orig,dest,fantasmas):
    
    camino = [orig]
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

    backtrack(laberinto,orig,dest,camino)

    return caminos_validos

for _ in range(n_rondas):
    pos_ini = tuple(map(int,input().split()))
    orig, dest, fantasmas =  pos_ini[0], pos_ini[1], pos_ini[2:]

    pildoras = 0
    while pildoras < 4:
        combs = combinations(fantasmas,4-pildoras)

        posible = False
        for comb in combs:
            if calcular_caminos(laberinto,orig,dest,comb):
                posible = True

        if posible:
            break

        pildoras += 1

    print(pildoras)
