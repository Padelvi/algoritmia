from typing import Tuple

def get_exam() -> Tuple[int,Tuple] | None:
    tests = int(input())
    if tests == 0:
        exit(0)
    probs = []
    for x in input().split(" "):
        x = float(x)
        if x > (1/3):
            probs.append(x)

    return (tests,tuple(probs))

while True:
    exam = get_exam()
    