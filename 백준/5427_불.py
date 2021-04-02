from sys import stdin
T = int(stdin.readline())
for tc in range(T):
    M,N = map(int,stdin.readline().split())
    maps = []
    fire=[]
    for r in range(N):
        tmp = list(map(str,stdin.readline().strip()))
        for c in range(M):
            if tmp[c] == '*':
                fire.append((r,c))

    print(maps)