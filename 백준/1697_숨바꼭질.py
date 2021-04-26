from sys import stdin
from collections import deque
N,K  = map(int,stdin.readline().split()) #수빈이, 동생
D = [99999999]*1000001
D[N] = 0
visit = [0]*1000001
q =deque([(D[N],N)]) #거리, 좌표
while q:
    w,u = q.popleft()
    visit[u] = 1
    if u == K:
        print(w)
        break
    if 0<=u*2<=1000000 and not visit[u*2]:
        if D[u*2] > w + 1:
            D[u*2] = w + 1
            q.append((D[u*2],u*2))
    if 0<=u+1<=100000 and not visit[u+1]:
        if D[u+1] > w+1:
            D[u+1] = w + 1
            q.append((D[u+1],u+1))
    if 0<=u-1<=100000 and not visit[u-1]:
        if D[u-1] > w + 1:
            D[u-1] = w + 1
            q.append((D[u-1],u-1))
