import sys
from sys import stdin
sys.setrecursionlimit(10**6)
def worm(r,c):
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<M and visit[nr][nc] == 0 and field[nr][nc] == 1:
            worm(nr,nc)

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,stdin.readline().split())
    field = [[0]*M for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    worm_cnt = 0
    #밭에 배추 심기
    for _ in range(K):
        n,m = map(int,stdin.readline().split())
        field[n][m] = 1
    for r in range(N):
        for c in range(M):
            if visit[r][c] == 0 and field[r][c] == 1:
                worm(r,c)
                worm_cnt += 1
    print(worm_cnt)


