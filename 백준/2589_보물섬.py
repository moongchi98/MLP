from sys import stdin
from collections import deque

def bfs(r,c):
    D_max = 0
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    D= [[0]*M for _ in range(N)]
    visit =[[0]*M for _ in range(N)]
    Q = deque([])
    Q.append((r,c))
    visit[r][c] = 1
    while Q:
        r,c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0 and arr[nr][nc] == 'L':
                D[nr][nc] = D[r][c] + 1
                visit[nr][nc] = 1
                Q.append((nr,nc)) #이거때문에 후보의 양이 달라져서 시간차이 나는듯..
                if D[nr][nc] > D_max:
                    D_max = D[nr][nc]
    return D_max
N,M = map(int,stdin.readline().split())
arr = [list(stdin.readline().strip()) for _ in range(N)]
result = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'L':
            result = max(result,bfs(r,c))
print(result)

