from collections import Counter

def formar_palindromo(letras: list, single: str = "") -> str:
    lista_letras = sorted(letras)
    s = ""
    for l in lista_letras:
        s += l
    return s+single+s[::-1]

for _ in range(int(input())):
    n, letras = input().split()
    n = int(n)
    counter = Counter(letras)

    impar: str = ""
    posible = True
    pares = []
    for letra, count in counter.items():
        if count % 2:
            if impar:
                posible = False
                break
            else:
                impar = letra
                pares.extend([letra]*(count//2))
        else:
            pares.extend([letra]*(count//2))

    if posible:
        print(formar_palindromo(pares,impar))
    else:
        print("LO SIENTO JULIA")