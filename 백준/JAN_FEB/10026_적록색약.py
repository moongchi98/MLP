import sys
from sys import stdin
sys.setrecursionlimit(10**6)
#bfs로 탐색 =>
def not_color_blind(r,c,color):
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0 and chart[nr][nc] == color:
            not_color_blind(nr,nc,color)
def find_blue(r,c):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0 and chart[nr][nc] == 'B':
            find_blue(nr,nc)
def color_blind(r,c):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and chart[nr][nc] != 'B':
            color_blind(nr, nc)

N = int(input())
chart = []
for _ in range(N):
    chart.append(list(map(str,stdin.readline().strip())))
dr = [1,-1,0,0]
dc = [0,0,-1,1]
visit = [[0]*N for _ in range(N)] #비색맹
visited = [[0]*N for _ in range(N)]
not_cnt = 0
color_cnt = 0
for r in range(N):
    for c in range(N):
        #색맹 아닌사람
        if visit[r][c] != 1 and chart[r][c]=='R':
            not_color_blind(r,c,'R')
            not_cnt += 1
        elif visit[r][c] != 1 and chart[r][c] == 'G':
            not_color_blind(r,c,'G')
            not_cnt += 1
        elif visit[r][c] != 1 and chart[r][c] == 'B':
            not_color_blind(r,c,'B')
            not_cnt += 1
for r in range(N):
    for c in range(N):
        #색맹인사람
        if visited[r][c] != 1 and chart[r][c] == 'B':
            find_blue(r,c)
            color_cnt += 1
        elif visited[r][c] != 1 and chart[r][c] != 'B':
            color_blind(r,c)
            color_cnt += 1
print(not_cnt, color_cnt)

