# from itertools import combinations

r="r"
d="d"

l_alcanzables = []
# precalculados = []
# def calcular_caminos(caminos_precalculados=None):
def calcular_caminos():
    # if not caminos_precalculados:
    #     caminos_precalculados = []
    
    resultados = []
    # alcanzables = dict()
    alcanzables = set()
    camino = []
    vistos = set()

    def backtrack(i,j):
        # Marcamos el punto (i,j) como visto
        vistos.add((i,j))

        # Caso base: hemos llegado al destino
        if i == nfil-1 and j == ncol-1:
            resultados.append(camino.copy())
            return

        # Only two options: right or down
        for opcion in (r,d):
            # Nuevos i y j
            if opcion == r:
                ni,nj = i+1,j
            else:
                ni,nj = i,j+1

            actual = m[i][j]
            nuevo = m[ni][nj]

            # Solo queremos pasar por puntos nuevos
            if (ni,nj) in vistos:
                continue

            # Paso 0: descartamos secuencias inválidas y marcamos los puntos como alcanzables
            if nuevo >= actual:
                print(f"At {camino} and just tried {opcion}")
                # alcanzables[(i,j)] = camino.copy()+[nuevo]
                alcanzables.add((i,j))
                continue

            # 1. Elegir: avanzar al siguiente
            camino.append(opcion)

            # 2. Explorar: continuar mediante "DFS"
            backtrack(ni,nj)

            # 3. Deshacer: backtracking
            camino.pop()

    # for camino in caminos_precalculados:
    #     backtrack(laberinto,orig,dest,camino)
    backtrack(0,0)

    l_alcanzables.append(alcanzables)
    return resultados


# def cortar_camino(camino: list[int], fantasmas: tuple[int]):
#     for i,node in enumerate(camino):
#         if node in fantasmas:
#             del camino[i:]


for _ in range(int(input())):
    nfil,ncol = map(int,input().split())
    m = []
    for _ in range(nfil):
        m.append(list(map(int,input().split())))
    print(calcular_caminos())
    print(l_alcanzables)