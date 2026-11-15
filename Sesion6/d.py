def ask(k: int) -> int:
    print(f"? {k}", flush=True)
    return int(input())

def respond(k: int) -> None:
    print(f"! {k}", flush=True)

for _ in range(int(input())):
    n = int(input())

    lo, hi = 1, n
    ans = 0

    while lo <= hi:
        m = (lo + hi) // 2
        pos = ask(m)

        if pos == m:
            ans = m
            break
        elif pos > m:
            lo = m + 1
        else:
            hi = m - 1

    respond(ans)