from sys import stdin
def bingo_check(r,c):
    global bingo_cnt
    #세로체크
    total = 0
    for i in range(5):
        total += visit[i][c]
    if total == 5:
        bingo_cnt += 1
    else:
        total = 0
    #가로체크
    for j in range(5):
        total += visit[r][j]
    if total == 5:
        bingo_cnt += 1
    else:
        total = 0
    #대각선체크
    if (r+c) == 4:
        for k in range(5):
            total += visit[k][4-k]
        if total == 5:
            bingo_cnt += 1
        else:
            total = 0
    elif r == c:
        for k in range(5):
            total += visit[k][k]
        if total == 5:
            bingo_cnt += 1
        else:
            total = 0


location =[0]*26
visit =[[0]*5 for _ in range(5)]
cnt = 0
bingo_cnt = 0
answer = []
for r in range(5):
    arr = list(map(int,stdin.readline().split()))
    for c in range(5):
        location[arr[c]] = (r,c)
for _ in range(5):
    tmp = list(map(int,stdin.readline().split()))
    for c in tmp:
        r,c = location[c]
        visit[r][c] = 1
        cnt += 1
        if cnt >= 5:
            bingo_check(r,c)
            if bingo_cnt == 3:
                answer.append(cnt)
print(answer[0])