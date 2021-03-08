from sys import stdin
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))
num.sort()
def comb(idx,sel):
    if idx==M:
        result.append(tuple(sel))
        return
    for i in range(N):
        comb(idx+1,sel+[num[i]])

result = []
comb(0,[])
result = list(set(result))
result.sort()
for r in result:
    print(*r)