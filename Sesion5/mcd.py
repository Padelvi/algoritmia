for _ in range(int(input())):
    def mcd(a,b):
        # Suponemos a > b
        if b==0:
            return a
        else:
            return mcd(b,a%b)

    x,y = map(int,input().split())
    x,y = max(x,y),min(x,y)
    print(mcd(x,y))