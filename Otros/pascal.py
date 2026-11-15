from functools import cache
from math import comb

@cache
def pascal(n: int):
    result = []
    for m in range(n+1):
        row = [comb(m,k) for k in range(m+1)]
        result.append(row)
    return result

def pprint(l: list):
    for elem in l:
        print(elem)

pprint(pascal(int(input())))