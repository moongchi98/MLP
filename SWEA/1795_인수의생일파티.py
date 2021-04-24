from collections import deque
def dijkstra(q,arr,d):
    while q:
        w, u = q.popleft()
        for next_w,next in arr[u]: #인접 정점들
            if d[next] > w + next_w:
                d[next] = w + next_w
                q.append((d[next],next))

T = int(input())
for tc in range(1,T+1):
    N,M,X = map(int,input().split())
    G1 =[[] for _ in range(N+1)]
    G2 = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v,w = map(int,input().split())
        G1[u].append((w,v)) #u에서 v로 가는데 걸리는 가중치
        G2[v].append((w,u)) #v에 도착하는데 걸리는 가중치
    go = [12345678]*(N+1) #가는 거리용 X부터니까 일차원  LIST 사용
    back = [12345678]*(N+1)
    go[X],back[X] = 0,0
    Q1 = deque([(0,X)])
    Q2 = deque([(0,X)])
    dijkstra(Q1,G1,go)
    dijkstra(Q2,G2,back)
    max_ans = 0
    for idx in range(1,N+1):
        if go[idx]+back[idx] > max_ans:
            max_ans = go[idx]+back[idx]
    print(f'#{tc} {max_ans}')