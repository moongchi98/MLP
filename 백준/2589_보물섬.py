from sys import stdin
from collections import deque

N,M = map(int,stdin.readline().split())
arr = [list(stdin.readline().strip()) for _ in range(N)]
print(arr)
Q = deque([])
D_max = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for r in range(N):
    for c in range(M):
        D =[[0]*M for _ in range(N)]
        visit = [[0]*M for _ in range(N)] #방문체크용
        if arr[r][c] == 'L':
            Q.append((r,c))
            while Q:
                r,c = Q.popleft()
                visit[r][c] = 1
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0 and arr[nr][nc] == 'L':
                        D[nr][nc] = D[r][c] + 1
                        Q.append((nr,nc))

print(D)

