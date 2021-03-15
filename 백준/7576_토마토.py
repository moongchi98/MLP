from collections import deque
from sys import stdin
M,N = map(int,stdin.readline().split())
tomatos = []
ripen = deque()
for r in range(N):
    tmp = list(map(int,stdin.readline().split()))
    for c in range(M):
        if tmp[c] == 1:
            ripen.append((r,c))
    tomatos.append(tmp)
def bfs():
    global date
    while ripen:
        r,c = ripen.popleft()
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and tomatos[nr][nc] == 0:
                tomatos[nr][nc] = 1
                ripen.append((nr,nc))
                D[nr][nc] = D[r][c] + 1
                if D[nr][nc] > date:
                    date = D[nr][nc]

date = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited= [[0]*M for i in range(N)]
D = [[0]*M for _ in range(N)]
bfs()
#출력하기
result = date
for i in range(N):
    for j in range(M):
        if tomatos[i][j] != 0:
            continue
        else:
            result = -1
            break
print(result)


