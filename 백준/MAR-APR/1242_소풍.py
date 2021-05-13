N,K,M = map(int,input().split())
tmp = M #m의 상대적 위치
round = 0
while round < N:
    #K 번째 위치가 될 때
    round += 1
    if K % (N - round + 1) == tmp % (N - round + 1):
        break
    else:
        tmp = tmp - K
        while tmp <= 0:
            tmp += (N - round+1)
print(round)

