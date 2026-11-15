from heapq import heapify, heappush, heappushpop
from collections import deque

class MaxHeap:
    def __init__(self,l=[]) -> None:
        h = [-x for x in l]
        heapify(h)
        self.heap = h

    def push(self,item):
        heappush(self.heap,-item)

    def pushpop(self,item) -> int:
        return -heappushpop(self.heap,-item)

    def __len__(self):
        return len(self.heap)

    def ma(self) -> int:
        return -self.heap[0]

    def remove(self, item: int) -> None:
        self.heap.remove(-item)
        heapify(self.heap)

class MinHeap:
    def __init__(self,l=[]) -> None:
        self.heap = l
        heapify(self.heap)

    def push(self,item):
        heappush(self.heap,item)

    def pushpop(self,item) -> int:
        return heappushpop(self.heap,item)

    def __len__(self):
        return len(self.heap)

    def mi(self) -> int:
        return self.heap[0]

    def remove(self, item: int) -> None:
        self.heap.remove(item)
        heapify(self.heap)

for _ in range(int(input())):
    n_flores, max_diff = map(int,input().split())
    puntuaciones = list(map(int,input().split()))

    minh = MinHeap()
    maxh = MaxHeap()

    q = deque()
    i = 0
    maxlen = 0

    seguir = True
    item = puntuaciones[i]

    while i < n_flores:
        if seguir:
            item = puntuaciones[i]
            q.append(item)
            minh.push(item)
            maxh.push(item)
        elif not q:
            seguir = True
            continue

        # Actualizamos máximo y mínimo
        q_max = maxh.ma()
        q_min = minh.mi()

        # Comprobar diferencias
        if q_max - q_min > max_diff:
            # Nos hemos pasado, quitamos por la izquierda hasta no pasarnos
            seguir = False
            item = q.popleft()
            maxh.remove(item)
            minh.remove(item)
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