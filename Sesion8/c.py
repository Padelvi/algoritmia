from sys import exit

n_admins, n_mesas, n_peleas = map(int,input().split())
peleas = []
for _ in range(n_peleas):
    peleas.append(tuple(map(int,input().split())))

def test(distribucion,l):
    
    if len(distribucion) < 2:
        return True

    for ai,aj in peleas:
        if ai >= l or aj >= l:
            continue
        if distribucion[ai-1] == distribucion[aj-1]:
            return False
    return True

distribucion = []
resultados = []

def backtrack(pos=0):
    # Caso base: guardar distribuciones correctas
    if pos == n_admins:
        if test(distribucion,pos+1):
            print(*distribucion)
            exit(0)
        return

    for mesa in range(1,n_mesas+1):
        # Descartamos casos
        if not test(distribucion,pos+1):
            continue

        # Paso 1: avanzamos
        distribucion.append(mesa)

        # Paso 2: probamos todos los casos en este nodo
        backtrack(pos+1)

        # Paso 3: retrocedemos
        distribucion.pop()

backtrack()

print("IMPOSIBLE")