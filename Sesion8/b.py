a,b,c = input().split()[::2]
palabras = (a,b,c)
letras = list(set(palabras[0]+palabras[1]+palabras[2]))
non_zero = set(palabra[0] for palabra in palabras if len(palabra) > 1)
d = {}
usados = [False] * 10
resultados = []

def es_letra_valida(letra, digito):
    if usados[digito]:
        return False
    if digito == 0 and letra in non_zero:
        return False
    return True

weights = {letra: 0 for letra in letras}
for palabra, sign in [(a, 1), (b, 1), (c, -1)]:
    place = 1
    for letter in reversed(palabra):
        weights[letter] += sign * place
        place *= 10

# Probar si una combinación es válida
def test(d: dict):
    total = 0
    for letra in letras:
        total += weights[letra] * d[letra]
    
    return total == 0

def format_solution(d: dict):
    s = f"{palabras[0]} + {palabras[1]} = {palabras[2]}"
    for letra, digito in d.items():
        s = s.replace(letra,str(digito))
    return s

# print(palabras,letras,non_zero)
def backtrack(i=0):
    # Caso base
    if i==len(letras):
        if test(d):
            resultados.append(format_solution(d))
        return

    letra = letras[i]
    for digito in range(10):
        # Paso 0: descartar
        if not es_letra_valida(letra,digito):
            continue

        # Paso 1: avanzar
        d[letra] = digito
        usados[digito] = True

        # Paso 2: probar todos los casos en esta rama del árbol
        backtrack(i+1)

        # Paso 3: volver atrás
        del d[letra]
        usados[digito] = False

backtrack()

if resultados:
    resultados.sort()
    for resultado in resultados:
        print(resultado)
else:
    print("IMPOSIBLE")