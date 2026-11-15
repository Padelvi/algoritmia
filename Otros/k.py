def get_shows():
    days = int(input())
    if days == 0:
        print("NO SE PUEDE")
        exit(0)
    shows = input().split(" ")
    return days,shows

def test_letters(l):
    sol = set()
    for letter in l:
        sol.add(letter)
        if len(sol) < 3:
            return True
    return False

# def loop(tests, shows) -> None:
#     x = tests // 2
#     sublists = (shows[:x],shows[x:])
#     if not test_letters(sublists[0]):
#         return loop(len(sublists[1]), sublists[1])
#     elif not test_letters(sublists[1]):
#         return loop(len(sublists[0]), sublists[0])
#     else:
#         return max(loop)

positions = {
    "C": -1,
    "H": -1,
    "R": -1
}

while True:
    days,shows = get_shows()
    for i in range(days):
        letter = shows[i]
        if positions[letter] == -1:
            positions[letter] = i
            continue
        