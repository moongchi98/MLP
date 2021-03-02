def number_check(x):
    for r in range(5):
        for c in range(5):
            if bingo[r][c] == x:
                bingo[r][c] = 0
                return (r,c)
def bingo_check(r,c):
    dr = [-1,1,0,0,-1,-1,1,1]
    dc = [0,0,-1,1,1,-1,1,-1]
    for i in range(8):
        cnt = 1
        nr = r + dr[i]
        nc = c + dc[i]
        while 0<=nr<5 and 0<=nc<5 and bingo[nr][nc] == 0:
            nr += dr[i]
            nc += dc[i]
            cnt += 1
            if cnt == 5:
                return 1
                break
    else:
        return 0

bingo =[]
for _ in range(5):
    bingo.append(list(map(int,input().split())))
numbers = []
for _ in range(5):
    tmp = list(map(int,input().split()))
    for t in tmp:
        numbers.append(t)
total = 0
#사회자가 부른 숫자 list의 idx로 몇번째의 빙고 성공인지 확인하기
#사회자가 부르는 숫자 반복문
for idx in range(len(numbers)):
    #호출된 숫자가 5개 미만이라면 굳이 확인할 필요 x
    if idx <= 4:
        number_check(numbers[idx])
    else:
        r = number_check(numbers[idx])[0]
        c = number_check(numbers[idx])[1]
        total += bingo_check(r,c)
        if total == 3:
            print(idx+1)
            break


