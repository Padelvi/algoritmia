from functools import cache

@cache
def bell(i,j):
    if j==0:
        if i==0:
            return 1
        else:
            return bell(i-1,i-1)
    else:
        return bell(i,j-1)+bell(i-1,j-1)

print(bell( int(input()), 0 ))