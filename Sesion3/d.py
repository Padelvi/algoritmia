n_planetas, n_disparos = map(int,input().split())
rebeldes = []
resto = []

for _ in range(n_planetas):
    x,y,r = map(int,input().split())
    if r:
        rebeldes.append((x,y))
    else:
        resto.append((x,y))
pi = list(map(int,input().split()))
    
print(rebeldes)
print(resto)
print(pi)