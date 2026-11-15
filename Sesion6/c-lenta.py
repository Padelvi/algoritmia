from collections import deque
from bisect import insort

for _ in range(int(input())):
    n_flores, max_diff = map(int,input().split())
    puntuaciones = list(map(int,input().split()))

    i = 0
    maxlen = 0
    q = deque()
    l = []
    q_min = float("+inf")
    q_max = float("-inf")

    seguir = True
    item = puntuaciones[i]

    while i < n_flores:
        if seguir:
            item = puntuaciones[i]
            q.append(item)
            insort(l,item)

            # Actualizar máximos y mínimos
            if item > q_max:
                q_max = item
            if item < q_min:
                q_min = item
        else:
            if not q:
                seguir = True
                continue
            q_max = l[-1]
            q_min = l[0]

        # Comprobar diferencias
        if q_max - q_min > max_diff:
            # Nos hemos pasado, quitamos por la izquierda hasta no pasarnos
            seguir = False
            item = q.popleft()
            l.remove(item)
        else:
            # Actualizamos maxlen
            num_flores = len(q)
            # print(q, q_max, q_min)
            if num_flores > maxlen:
                maxlen = num_flores
            seguir = True

        if seguir:
            i += 1

    print(maxlen)