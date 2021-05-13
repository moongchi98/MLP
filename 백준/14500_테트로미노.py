#시간초과
from sys import stdin
def combi(idx,total,q,i):
    global max_total,visit_check
    if i>=N*M or N*M-i<4-idx:
        return
    if idx == 4:
        if total > max_total:
            check(q[0],q)
            if sum(sum(visit_check,[])) == 4:
                max_total = total
            visit_check =[[0]*M for _ in range(N)]
        return
    tmp.append(i)
    combi(idx+1,total+arr[i],q+[i],i+1)
    tmp.pop()
    combi(idx,total,q,i+1)

def check(s,q):
    q = set(q)
    r = s // M
    c = s % M
    visit_check[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<M and visit_check[nr][nc] == 0:
            next = (nr*M+nc)
            if next in q:
                check(next,q)
N,M = map(int,stdin.readline().split())
arr =[]
for _ in range(N):
    arr += list(map(int,stdin.readline().split()))
visit = [0]*(N*M)
visit_check =[[0]*M for _ in range(N)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
tmp = []
max_total = 0
combi(0,0,[],0)
print(max_total)
N,M = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]
all_kind= [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]]

max_total = 0
total = 0
for i in range(N):
    for j in range(M):
        for s in all_kind:
            for x in range(4):
                nr = i + s[x][0]
                nc = j + s[x][1]
                if 0<=nr<N and 0<=nc<M:
                    total += arr[nr][nc]
            if total > max_total:
                max_total = total
            total = 0
print(max_total)