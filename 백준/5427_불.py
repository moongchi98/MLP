from sys import stdin
from collections import deque
#상근이 탈출용 bfs
def bfs():
    while q:
        r,c = q.popleft()
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0: #범위안에 있고
                if maps[nr][nc] == '.': #빈공간이면
                    q.append((nr,nc))
                    D[nr][nc] = D[r][c] + 1
            elif nr < 0 or nr >= N or nc < 0 or nc >= M:
                return D[r][c]
    fire()
    return -1
def fire():
    flen = len(fireq)
    while flen:
        r,c = fireq.popleft()
        visited[r][c] =1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0:
                if maps[nr][nc] == '.':
                    fireq.append((nr,nc))
                    maps[nr][nc] = '*'
        flen -= 1

T = int(stdin.readline())
for tc in range(T):
    M,N = map(int,stdin.readline().split())
    maps = []
    fireq, q=deque([]),deque([])
    visited=[[0]*M for _ in range(N)]
    D=[[0]*M for _ in range(N)]
    for r in range(N):
        tmp = list(map(str,stdin.readline().strip()))
        for c in range(M):
            if tmp[c] == '*':
                fireq.append((r,c))
            elif tmp[c] == '@':
                q.append((r,c))
                tmp[c] = '.'
        maps.append(tmp)
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    fire()
    answer = bfs()
    if answer != -1:
        print(answer+1)
    else:
        print("IMPPOSSIBLE")
