#결국 조합이군,,녀석..
#tc개수가 안주어진 경우 =>while문 돌리고 종료 조건으로 break
def combination(k):
    if len(chosen) == 6:
        chosen.sort()
        print(*chosen)
        chosen.clear()
    else:
        for i in range(k):
            if len(chosen) < 6 and visit[i] == 0:
                chosen.append(data[i])
                visit[i] = 1
                for j in range(i+1,k):
                    visit[j] = 0

while True:
    data = list(map(int,input().split()))
    if data[0] == 0:
        break
    k = data[0]
    chosen = []
    data = data[1::] #집합 S만
    data.sort()
    visit = [0] * k
    combination(k)
