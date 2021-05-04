from sys import stdin
from collections import deque
def dfs():
    cnt_y = 0
    ans = []
    while q:
        r,c = q.popleft()
        ans.append(arr[r][c])
        for dr,dc in d:
            nr = r + dr
            nc = c + dc
            if 0<=nr<5 and 0<=nc<5 and visit[nr][nc] == 0:
                if arr[nr][nc] == 'Y' and cnt_y <= 2:
                    q.append((nr,nc))
                    visit[nr][nc] = 1
                    cnt_y += 1
                elif arr[nr][nc] == 'S':
                    q.append((nr,nc))
                    visit[nr][nc] = 1
        if len(ans) == 7:
            if cnt_y < 4:
                print(ans)
                break
            else:
                ans =[]

arr = [list(stdin.readline().strip()) for _ in range(5)]
result = 0
d =[(-1,0),(1,0),(0,-1),(0,1)]
q = deque()
for r in range(5):
    for c in range(5):
        if arr[r][c] == 'S':
            visit = [[0] * 5 for _ in range(5)]
            q.append((r,c))
            visit[r][c] = 1
            dfs()
# print(result)

