from sys import stdin
N = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)] # 먼지 현황 받아오기
def spread(nx,ny,d): #모래 퍼트리기(y의 좌표, 이동 방향)
    print(nx,ny)
    global outside
    move_dust =[[(0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-2,0,0.02),(-1,0,0.07),(2,0,0.02),(-1,0,0.07),(1,1,0.01),(-1,1,0.01)],[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),(-1,1,0.1),(1,1,0.1),(0,2,0.05)],[(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),(-2,0,0.05),(0,-2,0.02),(0,2,0.02)],[(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(1,-1,0.1),(1,1,0.1),(2,0,0.05)]]
    to_alpha =[(0,-1),(0,1),(-1,0),(1,0)]
    for i in range(9):
        move = move_dust[d][i]
        nr = nx + move[0]
        nc = ny + move[1]
        if 0<=nr<N and 0<=nc<N:
            arr[nr][nc] += int(arr[nx][ny]*move[2])
        else:
            outside += int(arr[nx][ny]*move[2])
    ax = nx + to_alpha[d][0]
    ay = nx + to_alpha[d][1]
    if 0<=ax<N and 0<=ay<N :
        arr[ax][ay] += int(arr[nx][ny]*0.55)
    else:
        outside += int(arr[nx][ny] * 0.55)
    arr[nx][ny] = 0


x,y = N //2 , N // 2 #시작점
print('first',x,y)
round = 1 #몇번째 회전인지
dir = [(-1,0),(1,0),(0,-1),(0,1)]
outside = 0 #밖으로 나간애들
while True: #토네이도 이동 시키기
    print(round,'round')
    if round % 4 == 1: #홀수번째 라운드이면 열감소 행증가
        for i in range(1,(round % 4)+1): #
            print('left')# 왼쪽
            x += dir[2][0]
            y += dir[2][1]
            if x == 1 and y == 1:
                break
            else:
                spread(x,y,0)
    elif round % 4 == 2:
        for i in range(1,round % 4+1): #아래로 이동
            x += dir[1][0]
            y += dir[1][1]
            if x == 1 and y == 1:
                break
            else:
                spread(x, y, 3)
    elif round % 4 == 3:
        for i in range(1,round % 4+1):
            x += dir[3][0]
            y += dir[3][1]
            if x == 1 and y == 1:
                break
            else:
                spread(x,y,1)
    else:
        for i in range(1,round % 4+1):
            x += dir[0][0]
            y += dir[0][1]
            if x == 1 and y == 1:
                break
            else:
                spread(x,y,2)
    if x== 1 and y == 1:
        print('really out')
        break
    else:
        round += 1
print(outside)