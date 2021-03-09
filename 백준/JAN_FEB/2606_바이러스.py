# def bfs():
#     while queue:
#         v = queue.pop(0)
#         visit[v] = 1
#         for w in roads[v]:
#             if not visit[w]:
#                 visit[w] = 1
#                 queue.append(w)
#                 D[w] = D[v] + 1
# N = int(input())
# E = int(input())
# roads = [[] for _ in range(N+1)]
# for _ in range(E):
#     s,e = map(int,input().split())
#     roads[s].append(e)
#     roads[e].append(s)
# visit = [0]*(N+1)
# queue = [1] #시작점
# D = [0] *(N+1)
# bfs()
# cnt = 0
# for i in D:
#     if i != 0:
#         cnt += 1
# print(cnt)

#dfs방법
def dfs(v):
    visit[v] = 1
    for w in roads[v]:
        if not visit[w]:
            stack.append(w)
            dfs(w)

N = int(input())
E = int(input())
roads = [[] for _ in range(N+1)]
for _ in range(E):
    s,e = map(int,input().split())
    roads[s].append(e)
    roads[e].append(s)
visit = [0]*(N+1)
stack = []
dfs(1)

print(sum(visit)-1) #1자기 자신은 빼줘야 하니까
