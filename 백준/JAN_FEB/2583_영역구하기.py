def change(a,b): #
    r,c = b,a
    r = N - r
    return(r,c)
def bfs(area):
    global cnt
    dr = [-1,1,0,0] #상,하,좌,우
    dc = [0,0,-1,1]

    while queue:
        r,c = queue.pop(0)
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                queue.append((nr,nc))
                visited[nr][nc] = 1
                area += 1
    cnt += 1
    return area

N, M, K = map(int,input().split())
arr = [[0]*M for _ in range(N)] #전체 사각형 만들어주기

for _ in range(K):
    ly,lx,ry,rx=map(int,input().split())
    r1,c1 = change(ly,lx)
    r2,c2 = change(ry,rx)
    for i in range(r2,r1):
        for j in range(c1,c2):
            arr[i][j] = 1
queue = []
result = []
cnt = 0 #영역의 개수
visited = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0 and visited[r][c] == 0:
            queue.append((r,c))
            result.append(bfs(1))
print(cnt)
result.sort()
print(*result)