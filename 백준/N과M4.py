from sys import stdin
N,M = map(int,stdin.readline().split())
def comb(idx,sel):
    if idx==M:
        print(*sel)
        return
    for i in range(N):
        if len(sel) == 0 or sel[-1] <= num[i]:
            comb(idx+1,sel+[num[i]])

num = [i for i in range(1, N + 1)]
comb(0, [])