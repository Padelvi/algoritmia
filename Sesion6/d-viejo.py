def ask(k: int) -> int:
    print(f"? {k}", flush=True)
    return int(input())

def respond(k: int) -> None:
    print(f"! {k}", flush=True)

for _ in range(int(input())):
    n = int(input())
    m = n//2
    preguntados = []
    tolerar = 1

    while True:
        if m == 0:
            num = ask(1)
            res = 1 if num==1 else 0
            respond(res)
            break
        if m in preguntados:
            if tolerar:
                tolerar -= 1
            else:
                respond(0)
                break
        else:
            preguntados.append(m)

        pos = ask(m)

        if pos > m:
            m = (n+m)//2
        elif pos < m:
            m = (1+m)//2
        else:
            respond(m)
            break