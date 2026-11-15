from heapq import heappush, heappushpop

class MaxHeap:
    def __init__(self) -> None:
        self.heap = list()

    def push(self,item):
        heappush(self.heap,-item)

    def pushpop(self,item):
        return -heappushpop(self.heap,-item)

    def __getitem__(self, key):
        return -self.heap.__getitem__(key)

    def __len__(self):
        return len(self.heap)

def pprint(x):
    if x==int(x):
        print(float(x))
    else:
        print(x)

def running_median(iterable):
    lo = MaxHeap()  # max-heap
    hi = []  # min-heap (same size as or one smaller than lo)

    for x in iterable:
        # print(lo.heap, hi)
        if len(lo) == len(hi):
            lo.push(heappushpop(hi, x))
            yield lo[0]
        else:
            heappush(hi, lo.pushpop(x))
            yield (lo[0] + hi[0]) / 2

for _ in range(int(input())):
    n_ini, n_adicionales = map(int,input().split())
    nums = list(map(int,input().split()))

    for _ in range(n_adicionales):
        nums.append(int(input()))

    i = 0
    for med in running_median(nums):
        if i >= n_ini-1:
            pprint(med)
        i += 1