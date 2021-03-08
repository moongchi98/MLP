from sys import stdin
#bfs로 탐색 =>
def not_color_blind(r,c):
    visit[r][c] = 1
    for i in range(4):
        if 0<=nr<N and 0<=nc<N


N = int(input())
chart = []
for _ in range(N):
    chart.append(list(map(int,stdin.readline().strip())))
dr = [1,-1,0,0]
dc = [0,0,-1,1]
visit = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        #'R'의 구역 찾기
        if visit[r][c] != 1 and chart[r][c]=='R':
            not_color_blind(r,c)

