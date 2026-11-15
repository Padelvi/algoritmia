from bisect import insort

def med(l: list[int], n: int):
    pos_med = n/2
    if int(pos_med) == pos_med:
        pos_med = int(pos_med)
        # item = round((l[pos_med]+l[pos_med-1])/2,1)
        item = (l[pos_med]+l[pos_med-1])/2
    else:
        pos_med = int(pos_med)
        item = l[pos_med]
    return item

def pprint(x):
    if isinstance(x,int):
        print(f"{x}.0")
    else:
        print(x)

for _ in range(int(input())):
    n_ini, n_adicionales = map(int,input().split())
    nums = sorted(map(int,input().split()))
    pos_med = n_ini/2
    pprint(med(nums,n_ini))

    for _ in range(n_adicionales):
        n_ini += 1
        adicional = int(input())
        insort(nums,adicional)
        pprint(med(nums,n_ini))
