N = int(input())
palette = [[-1]*101 for _ in range(101)]
for idx in range(N):
    c,r,w,h = map(int,input().split())
    c,r = r,c
    r = 100 - r

    #왼쪽 아래 좌표가 주어지는 거니까
    for i in range(w):
        for j in range(h):
            nr = r - i
            nc = c + j
            palette[nr][nc] = idx

for idx in range(N):
    cnt = 0
    for r in range(101):
        for c in range(101):
            if palette[r][c] == idx:
                cnt += 1
    print(cnt)