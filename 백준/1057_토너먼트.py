def next_round(num):
    if num % 2 :
        num = int((num+1) / 2)
    else:
        num = int((num)/2)
    return num

N, kim, lim = map(int,input().split())
#같은 round인지 확인하기
cnt = 1
while True:
    if next_round(kim) == next_round(lim):
        print(cnt)
        break
    else:
        kim = next_round(kim)
        lim = next_round(lim)
        cnt += 1
        if kim == 0 or lim == 0:
            print(-1)
            break



