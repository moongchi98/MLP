from sys import stdin
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))
num.sort()
def comb(idx,sel):
    if idx==M:
        print(*sel)
        return
    for i in range(N):
            comb(idx+1,sel+[num[i]])
comb(0, [])