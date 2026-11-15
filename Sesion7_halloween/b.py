for _ in range(int(input())):
    s = input()
    if s[::2] == s[1::2]:
        print(s[::2])
    else:
        print("IMPOSIBLE")