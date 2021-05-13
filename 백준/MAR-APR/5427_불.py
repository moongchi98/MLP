from sys import stdin
from collections import deque
def bfs():
    while q:
        q_len = len(q)
        for j in range(q_len):
            r,c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<N and 0<=nc<M:
                    if maps[nr][nc] == '.' and D[nr][nc] == 0: #분기처리 중요..
                        q.append((nr,nc))
                        D[nr][nc] = D[r][c] + 1
                elif 0>nr or nr==N or 0>nc or M==nc:
                    print(D[r][c]+1)
                    return
        fire()
    print("IMPOSSIBLE")
    return

def fire():
    fire_len = len(fireq)
    for j in range(fire_len):
        r,c = fireq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if maps[nr][nc] == '.':
                    fireq.append((nr,nc))
                    maps[nr][nc] = '*'


T = int(stdin.readline())
for _ in range(T):
    M,N = map(int,stdin.readline().split())
    fireq = deque([])
    q = deque([])
    maps= []
    D = [[0]*M for _ in range(N)]
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
    bfs()