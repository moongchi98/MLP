from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def safe_area(r,c,j,area):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0 and city[nr][nc] > j:
            visit[nr][nc] = 1
            safe_area(nr,nc,j,area+1)

N = int(stdin.readline())
city = []
min_value = 999
max_value = 0
for _ in range(N):
    tmp = list(map(int,stdin.readline().split()))
    for x in tmp:
        if x > max_value:
            max_value = x
        elif x < min_value:
            min_value = x
    city.append(tmp)
max_cnt = 1

for j in range(min_value,max_value):
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if city[r][c] > j and visit[r][c] == 0:
                safe_area(r,c,j,1)
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)

