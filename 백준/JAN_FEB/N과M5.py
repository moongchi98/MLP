from sys import stdin
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))
num.sort()
def comb(idx,sel):
    if idx==M:
        print(*sel)
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            comb(idx+1,sel+[num[i]])
            visit[i] = 0
visit = [0]*N
comb(0, [])