def sumCifras(a: int):
    return sum((int(c) for c in str(a)))

for _ in range(int(input())):
    a = int(input())
    i = a
    while True:
        if sumCifras(i) % 4 == 0:
            print(i)
            break
        i += 1