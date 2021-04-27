from sys import stdin
from collections import deque
def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1#처음시작점
    while q:
        v = q.popleft()
        for next in G[v]:
            if visit[next] == 0:
                visit[next] = -v
                q.append(next)
            elif visit[next] == visit[v]:
                return False
    return True

T = int(stdin.readline())
for tc in range(T):
    V,E = map(int,stdin.readline().split())
    G =[[] for _ in range(V+1)]
    visit=[0]*(V+1)
    flag = 'YES'
    for _ in range(E):
        u,v = map(int,stdin.readline().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(1,V+1):
        if visit[i] == 0:
            if not bfs(i):
                flag = 'NO'
                break
    print(flag)









