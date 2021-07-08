from sys import stdin
from collections import deque
def bfs(q):
    global countries
    tmp = [] #한개의 연합국 찾기
    #연결된 연합애들 모두 찾기
    while q:
        r,c = q.popleft()
        visit[r][c] = 1
        for i in range(4):
            nr = r + d[i][0]
            nc = c + d[i][1]
            if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0:
                diff = abs(arr[r][c] - arr[nr][nc])
                if L<=diff<=R:
                    visit[nr][nc] = 1
                    q.append((nr,nc))
                    tmp.append((nr,nc))
                    tmp.append((r,c))
    tmp = list(set(tmp))

    if tmp != []:
        people = 0
        for next in tmp:
            people += arr[next[0]][next[1]]
        new_people = people // len(tmp)
        for n in tmp:
            arr[n[0]][n[1]] = new_people  # 새로운 인원수 할당
        countries += 1


N,L,R = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]
d = [(1,0),(0,1),(-1,0),(0,-1)]
cnt = 0
while True:
    visit = [[0]*N for _ in range(N)]
    countries = 0 # 인접 국가 개수
    #하루동안 국경 열리는 애들 조사하기
    for r in range(N):
        for c in range(N):
            if visit[r][c] == 0: #아직 방문안했따면
                q = deque([(r,c)])
                visit[r][c] = 1
                bfs(q)
    #연합국 인원 조정
    if countries == 0:
        break
    else:
        cnt += 1
print(cnt)