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
            if len(sel) == 0 or sel[-1]<=num[i]:
                comb(idx+1,sel+[num[i]])
            for j in range(i+1,N):
                visit[j] = 0
visit = [0]*N
comb(0, [])