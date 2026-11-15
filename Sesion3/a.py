if __name__ == "__main__":
    for _ in range(int(input())):
        num =  int(input())
        l = sorted([ int(i) for i in input().split(" ") ])
        diffs = []
        elems = []
        for i in range(1,num):
            diffs.append(l[i]-l[i-1])
        print(min(diffs))