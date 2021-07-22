from sys import stdin
from collections import deque
def find_next(q):
    min_time = 123456789 #그 칸까지 가는데 걸리는 최소시간
    global baby_shark
    next = []
    visit = [[0]*N for _ in range(N)]
    while q:
        r,c = q.popleft()
        visit[r][c] = 1
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<N and 0<=nc<N and not visit[nr][nc]:
                if arr[nr][nc] == 0:
                    D[nr][nc] = D[r][c] + 1 # 물고기없으면 그냥 통과
                    q.append((nr,nc))
                elif 0<arr[nr][nc] < baby_shark: #현재 아기상어보다 작다면
                    D[nr][nc] = D[r][c] + 1 #그 칸 통과하는데 걸리는 시간
                    if D[nr][nc] < min_time:
                        min_time = D[nr][nc]
                        next = [(nr,nc)]#후보로 삽입
                    elif D[nr][nc] == min_time:
                        next.append((nr,nc))
                    q.append((nr,nc))
                elif arr[nr][nc] == baby_shark: #크기 같으면 통과만
                    D[nr][nc] = D[r][c] + 1
                    q.append((nr,nc))
                visit[nr][nc] = 1
    # print(next)
    return next

def shortest(dq):
    visit = [[0] * N for _ in range(N)]
    while dq:
        x,y = dq.popleft()
        visit[x][y] = 1
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0<=nr<N and 0<=nc<N and not visit[nr][nc]:
                if arr[nr][nc] == 0:
                    D[nr][nc] = D[r][c] + 1
                    dq.append((nr,nc))
                elif D[nr][nc] != 9:
                    D[nr][nc] = D[r][c] + 1
                    print((nr,nc))
                    return(nr,nc)


N = int(stdin.readline())
arr =[] # 전체 list
fish =0 #물고기 먹은 수
for r in range(N):
    tmp = list(map(int,stdin.readline().split()))
    for c in range(N):
        if tmp[c] == 9:
            sr,sc = r, c # 시작점
    arr.append(tmp)
baby_shark = 2
time = 0 #엄마 도움 시간 전에

while True:
    D = [[0]*N for _ in range(N)] #거리확인용
    q_list = deque([(sr,sc)])
    pr = sr
    pc = sc
    # if fish == 1:
    #     print(q_list,sr,sc)
    #     lr,lc = shortest(q_list)
    #     time += D[lr][lc]
    cand = find_next(q_list) #후보애들
    if len(cand) == 0:
        break
    elif len(cand) > 1: #하나 이상있을 경우
        delta = 123948
        min_nx = 1234948
        next_cand = []
        for nx,ny in cand:
            if nx < min_nx : #가장 위쪽에 있는 애들
                min_nx = nx
                pr = nx
                pc = ny
                next_cand =[(nx,ny)]
            elif nx == min_nx:
                next_cand.append((nx,ny))
        if len(next_cand) > 1:
            for px,py in next_cand:
                if py < sc and (sc-py) < delta : #왼쪽에 있는애로 설정
                        delta = sc-py
                        pr = px
                        pc = py
    elif len(cand) == 1:
        pr = cand[0][0]
        pc = cand[0][1]

    arr[pr][pc] = 9 #물고기 먹음
    arr[sr][sc] = 0 #있던자리 먹은거 처리
    sr = pr
    sc = pc
    time += D[sr][sc] #이동한 시간
    fish += 1 #먹은 물고기수
    if fish == baby_shark:
        baby_shark += 1
        fish = 0
    # print('size',baby_shark)
print(time)

