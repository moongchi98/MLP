from sys import stdin
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))
num.sort()
def comb(idx,sel):
    if idx==M:
        result.append(tuple(sel))
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            if len(sel) == 0 or sel[-1] <= num[i]:
                comb(idx+1,sel+[num[i]])
            visit[i] = 0
visit = [0]*N
result = []
comb(0,[])
result = list(set(result))
result.sort()
for r in result:
    print(*r)
