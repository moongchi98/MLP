from sys import stdin
def find():
    while zero_list:
        r,c = zero_list.pop(0)
        #세로줄 탐색
        cnt = 0
        total = 45
        for i in range(0,9):
            total -= sdoku[i][c]
            if sdoku[i][c] == 0:
                cnt += 1
        if cnt == 1:
            sdoku[r][c] = total
            continue
        else:
            cnt = 0
            total = 45
        #가로줄 탐색
        for i in range(0,9):
            total -= sdoku[r][i]
            if sdoku[r][i] == 0:
                cnt += 1
        if cnt == 1:
            sdoku[r][c] = total
            continue
        else:
            cnt = 0
            total = 45
        #3*3탐색
        nr = r//3 * 3
        nc = c//3 * 3
        for i in range(3):
            for j in range(3):
                total -= sdoku[nr+i][nc+j]
                if sdoku[nr+i][nc+j] == 0:
                    cnt += 1
        if cnt == 1:
            sdoku[r][c] = total
            continue
        else:
            cnt = 0
            total = 45
        if sdoku[r][c] == 0:
            zero_list.append((r,c))
sdoku = []
for _ in range(9):
    sdoku.append(list(map(int,stdin.readline().split())))
#0인 애들 찾아주기
zero_list = []
for r in range(9):
    for c in range(9):
        if sdoku[r][c] == 0:
            zero_list.append((r,c))
find()
for s in sdoku:
    print(*s)