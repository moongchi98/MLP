from sys import stdin
import heapq
def dijkstra(start):
    q = []
    D = [123456789] * (N + 1)
    D[start] = 0
    heapq.heappush(q,(D[start],start))
    while q:
        w, p = heapq.heappop(q)
        for next_p, next_w in G[p]:
            if D[next_p] > next_w + w:
                D[next_p] = next_w + w
                heapq.heappush(q, (D[next_p], next_p))
    return D

N,E = map(int,stdin.readline().split())
G= [[] for _ in range(N+1)]
total1 = total2 = 0
for _ in range(E):
    u,v,w = map(int,input().split())
    G[u].append((v,w))
    G[v].append((u,w))
#1번에서 V1,V2중 어느점을 거치는게 빠른지 확인
v1,v2 = map(int,stdin.readline().split())
arr = [1,v1,v2,N]
tmp = [1,v2,v1,N]
for i in range(3):
    if dijkstra(arr[i])[arr[i+1]] == 123456789:
        total1 = -1
        break
    else:
        total1 += dijkstra(arr[i])[arr[i+1]]
for i in range(3):
    if dijkstra(tmp[i])[tmp[i+1]] == 123456789:
        total2 = -1
        break
    else:
        total2 += dijkstra(tmp[i])[tmp[i+1]]
total = min(total1,total2)
print(total)
