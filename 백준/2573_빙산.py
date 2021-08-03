from sys import stdin
from collections import deque
def melting(): #빙산 녹는 함수
    melt = [[0]*M for _ in range(N)] #매년 녹아야 하는 빙산의 개수
    while iceberg:
        r,c = iceberg.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0: #범위안이고, 바다라면
                melt[r][c] += 1
    for x in range(N):
        for y in range(M):
            arr[x][y] -= melt[x][y]
            if arr[x][y] <= 0 :
                arr[x][y] = 0
            else:
                iceberg.append((x,y))

def cnt_iceberg(): #빙산의 개수 세기
    global cnt
    if len(iceberg) == 0:
        return 0
    else:
        q = deque([(iceberg[0])])
        while q:
            x,y = q.popleft()
            cnt += 1
            visited[x][y] = 1
            for i in range(4):
                nr = x + dr[i]
                nc = y + dc[i]
                if 0<=nr<N and 0<=nc<M:
                    if not visited[nr][nc] and arr[nr][nc] != 0:
                        visited[nr][nc] = 1
                        q.append((nr,nc))
        return 1


N,M = map(int,stdin.readline().split())
arr = []
iceberg=deque([])
for r in range(N):
    tmp =list(map(int,stdin.readline().split()))
    for c in range(M):
        if tmp[c] != 0:
            iceberg.append((r,c))
    arr.append(tmp)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
year = 0
while True:
    visited=[[0]*M for _ in range(N)]
    cnt = 0 #빙하 개수
    melting()
    year += 1
    if cnt_iceberg():
        if cnt < len(iceberg):
            print(year)
            break
    else:
        print(0)
        break

