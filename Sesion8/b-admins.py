a, _, b, _, c = input().split()

words = [a, b, c]
letters = sorted(set(a + b + c))
non_zero = {word[0] for word in words if len(word) > 1}

# convertir en una ecuacion
weights = {letter: 0 for letter in letters}
for word, sign in [(a, 1), (b, 1), (c, -1)]:
    place = 1
    for letter in reversed(word):
        weights[letter] += sign * place
        place *= 10

digits = {}
used = [False] * 10
solutions = []


def is_valid():
    total = 0
    for letter in letters:
        total += weights[letter] * digits[letter]
    return total == 0


def gen_solution():
    parts = []
    for word in words:
        number = ""
        for letter in word:
            number += str(digits[letter])
        parts.append(number)
    return f"{parts[0]} + {parts[1]} = {parts[2]}"


def is_valid_char(letter, digit):
    if used[digit]:
        return False
    if digit == 0 and letter in non_zero:
        return False
    return True


def solve(index):
    # base case por ser una función recursiva
    if index == len(letters):
        # si tenemos asignado a todas las letras numeros
        # compramos si resuelve la ecuacion
        if is_valid():
            solutions.append(gen_solution())
        return

    letter = letters[index]
    for digit in range(10):  # probamos todos los numeros
        if not is_valid_char(letter, digit):
            continue
        # probamos un numbero
        digits[letter] = digit
        used[digit] = True

        solve(index + 1)  # llamada recursiva donde esta la magia

        # desacemos el cambio
        used[digit] = False
        digits[letter] = -1


solve(0)  # empezamos por la primera letra siempre
solutions.sort()
if solutions:
    for solution in solutions:
        print(solution)
else:
    print("IMPOSIBLE")
