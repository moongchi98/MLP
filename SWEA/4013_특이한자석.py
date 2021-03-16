from collections import deque
def round(n,d):
    #회전하는애 양 옆 탐색
    left_c = n-1 #왼쪽 자석
    right_c = n + 1 #오른쪽 자석
    if 0<=left_c:
        if arr[n][6] != arr[left_c][2] and visit[left_c][2]== 0:
            visit[left_c][2] =1
            visit[n][6] = 1
            #왼쪽 자석 반대방향으로 회전하기 전에 옆에 녀석 탐색
            round(left_c,-d)
    if right_c<4:
        if arr[n][2] != arr[right_c][6] and visit[right_c][6] == 0:
            visit[right_c][6] = 1
            visit[n][2] = 1
            round(right_c,-d)
    if d == 1: #반시계방향
        x = arr[n].pop()
        arr[n].insert(0,x)
        return
    else:
        x = arr[n].popleft()
        arr[n].append(x)
        return

def score():
    global total
    for i in range(4):
        if arr[i][0] == 0:
            total += 0
        elif arr[i][0] == 1:
            total += (2**i)


T = int(input())
for tc in range(1,T+1):
    K = int(input())
    arr = []
    total = 0
    for _ in range(4):
        tmp = deque(list(map(int,input().split())))
        arr.append(tmp)
    for _ in range(K):
        n, d = map(int,input().split())
        visit=[[0]*7 for _ in range(4)]
        round(n-1,d)
    score()
    print('#{} {}'.format(tc,total))



