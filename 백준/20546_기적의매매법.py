from sys import stdin
def BNP(money,cnt):
    for i in range(14):
        can_buy = int(money / chart[i])
        if can_buy == 0:
            continue
        else:
            money = money - (can_buy * chart[i])
            cnt += can_buy
    left = (cnt * chart[13] + money)
    return left

def TIMING(money,cnt):
    #올라가는 경향을 파악해야한다.
    up = down = 0
    idx = 1
    while idx < 14:
        if chart[idx] < chart[idx-1]:
            up = 0
            down += 1
            if down >= 3:
                can_buy = int(money / chart[idx])
                money = money - (can_buy * chart[idx])
                cnt += can_buy
        elif chart[idx] > chart[idx-1]:
            down = 0
            up += 1
            if up == 3:
                money += cnt * chart[idx]
                up = cnt = 0
        else:
            up = down = 0
        idx += 1
    left = (cnt * chart[13] + money)
    return left

money = int(stdin.readline())
chart = list(map(int,stdin.readline().split()))
jun = BNP(money,0)
sung = TIMING(money,0)
if jun > sung:
    print("BNP")
elif jun == sung :
    print("SAMESAME")
else:
    print("TIMING")