from sys import stdin
from itertools import combinations
N,M =map(int,stdin.readline().split())
arr = []
chicken = []
home = []
for r in range(N):
    tmp = list(map(int,stdin.readline().split()))
    for c in range(N):
        if tmp[c] == 2:
            chicken.append((r,c))
        elif tmp[c] == 1:
            home.append((r,c))
comb = list(combinations(chicken,M))

min_total = 123456789
for next in comb: #치킨집 3개
    D = [[123456789]*N for _ in range(N)]
    for nr,nc in next:
        for nx,ny in home:
            length = abs(nr-nx)+ abs(nc-ny)
            if D[nx][ny] > length:
                D[nx][ny] = length
    total = 0
    for r in range(N):
        for c in range(N):
            if D[r][c] != 123456789:
                total += D[r][c]
    if total < min_total:
        min_total = total
print(min_total)

