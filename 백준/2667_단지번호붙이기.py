from sys import stdin
#아파트인지 확인하기
def check(r,c): #재귀사용하면 stack 필요 없는듯
    global size
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and visit[nr][nc] != 1 and village[nr][nc] == 1:
            size += 1
            check(nr,nc)


N = int(input())
village = []
for _ in range(N):
    village.append(list(map(int,stdin.readline().strip())))
dr = [-1,1,0,0]
dc = [0,0,-1,1]
visit = [[0]*N for _ in range(N)]
result= []
for r in range(N):
    for c in range(N):
        if village[r][c] ==1 and visit[r][c] != 1:
            size = 1
            check(r,c)
            result.append(size)
print(len(result))
result.sort()
for r in result:
    print(r)



