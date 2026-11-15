def hanoi(n,postes="ABC"):
    # Función auxiliar para imprimir los movimientos
    def mover(x,y):
        return f"{x} {y}",

    # Caso base y recursión
    if n == 1:
        return mover(postes[0],postes[2])
    else:
        return (
        *hanoi(n-1,postes[0]+postes[2]+postes[1]),
        *mover(postes[0],postes[2]),
        *hanoi(n-1,postes[1]+postes[0]+postes[2]),
        )

for _ in range(int(input())):
    n = int(input())
    h = hanoi(n)
    l = len(h)
    print(l)
    for t in h:
        print(t)