from sys import stdin
from collections import deque
def bfs():
    visit =[[123456789]*M for _ in range(N)]
    visit[0][0] = 0
    while q:
        r,c = q.popleft()
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0<=nr<N and 0<=nc<M:
                if visit[nr][nc] > visit[r][c] + arr[nr][nc]:
                    visit[nr][nc] = visit[r][c] + arr[nr][nc]
                    q.append((nr,nc))
    return visit[N-1][M-1]



M,N = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().strip())) for _ in range(N)]
q = deque()
q.append((0,0))
print(bfs())

