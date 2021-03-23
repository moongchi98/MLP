from sys import stdin

def choice(idx,max_ability,id):
    global total
    if idx == 11:
        visit[id] = 1 #포지션 배정 되었다고 표시하기
        total += max_ability
        return
    if arr[r][idx] > max_ability and arr[r][idx] != 0 and visit[idx] == 0:
        max_ability = arr[r][idx]
        id = idx
        choice(idx+1,max_ability, id)
        max_ability = 0
        id = 0
    else:
        choice(idx+1,max_ability,id)

T = int(stdin.readline())
arr =[]
for _ in range(11):
    arr.append(list(map(int,stdin.readline().split())))
visit =[0]*11
total = 0
for r in range(11):
    choice(0,0,0)
print(total)

