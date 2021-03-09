def boy(num):
    for i in range(num-1,switch,num):
        # 배수들만이니까 간격을 아예 num으로 설정
        if status[i] == 1:
            status[i] = 0
        else:
            status[i] = 1
    return status

def girl(num):
    num -= 1
    if status[num] == 0:
        status[num] = 1
    else:
        status[num] = 0
    i = 1
    while num-i>=0 and num+i<switch and status[num-i] == status[num+i]:
        if status[num+i] == 0:
            status[num+i] = 1
            status[num-i] = 1
        else:
            status[num+i] = 0
            status[num-i] = 0
        i += 1
    return status

switch = int(input()) #개수
status = list(map(int,input().split())) #스위치 초기 상태
N = int(input()) #학생수
for _ in range(N):
    gender,num = map(int,input().split())
    if gender == 1:
        status = boy(num)
    else:
        status = girl(num)
for i in range(0,switch,20):
    print(*status[i:i+20])