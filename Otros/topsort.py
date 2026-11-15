def canFinish(prerequisites: list[list[int]]) -> bool:
    d = {}
    for (a,b) in prerequisites:
        if a in d:
            d[a].append(b)
        else:
            d[a] = [b]

    print(d)
    from graphlib import TopologicalSorter, CycleError

    try:
        tuple(TopologicalSorter(d).static_order())
    except CycleError:
        return False
    else:
        return True

print(canFinish([[1,0]]))
print(canFinish([[1,0],[0,1]]))