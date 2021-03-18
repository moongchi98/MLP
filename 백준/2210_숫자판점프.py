from sys import stdin
def bfs(r,c,idx,num):
    if idx == 6:
        result.add(num)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<5 and 0<=nc<5:
            bfs(nr,nc,idx+1,num+str(numbers[r][c]))

numbers = []
for _ in range(5):
    numbers.append(list(map(int,stdin.readline().split())))
dr = [-1,1,0,0]
dc = [0,0,-1,1]
result = set()
for r in range(5):
    for c in range(5):
        bfs(r,c,0,"")
print(len(result))