from sys import stdin
T = int(stdin.readline())

for tc in range(T):
    N = int(stdin.readline())
    sr, sc = map(int,stdin.readline().split())
    er, ec = map(int,stdin.readline().split())
    #8방향
    dr = [-1,-2,-2,-1,1,2,2,1]
    dc = [2,1,-1,-2,-2,-1,1,2]
    queue = [(sr,sc)]
    visited =[[0]*N for _ in range(N)]
    D = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1
    D[sr][sc] = 1
    while queue:
        r,c = queue.pop(0)
        if r == er and c == ec:
            break
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
                D[nr][nc] = D[r][c] + 1
                queue.append((nr,nc))
                visited[nr][nc]= 1

    print(D[r][c]-1)