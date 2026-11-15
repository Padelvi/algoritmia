for _ in range(int(input())):
    num_billetes = int(input())
    billetes = sorted(map(int,input().split()))
    num_precios = int(input())
    try:
        precios = list(map(int,input().split()))
    except EOFError:
        print("---")
    else:
        for precio in precios:
            if num_billetes == 0:
                print(-1)
                continue
            if billetes[-1] < precio:
                print(-1)
                continue
            for billete in billetes:
                diff = billete - precio
                if diff >=0:
                    print(diff)
                    break

    print("---")
    # del precios