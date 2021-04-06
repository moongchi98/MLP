from sys import stdin
from collections import deque
def bfs(zero_count):
    global max_d
    while tomato:
        z,y,x = tomato.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nz<H and 0<=ny<N and 0<=nx<M and field[nz][ny][nx] == 0  :
                field[nz][ny][nx] = 1
                D[nz][ny][nx] = D[z][y][x] + 1
                if D[nz][ny][nx] > max_d:
                    max_d = D[nz][ny][nx]
                tomato.append((nz,ny,nx))
                zero_count -= 1
    return zero_count

M,N,H = map(int,stdin.readline().split())
field =[[] for _ in range(H)]
D =[[[0]*M for _ in range(N)] for _ in range(H)]
tomato = deque([])
zero_count = 0
max_d = 0
dy = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
for z in range(H):
    for y in range(N):
        tmp = list(map(int,stdin.readline().split()))
        for x in range(M):
            if tmp[x] == 1:
                tomato.append((z,y,x))
            elif tmp[x] == 0:
                zero_count += 1
        field[z].append(tmp)
if zero_count == 0:
    answer = 0
else:
    zero = bfs(zero_count)
    if zero == 0:
        answer = max_d
    else:
        answer = -1
print(answer)




