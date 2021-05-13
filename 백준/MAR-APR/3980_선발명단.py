from sys import stdin

def choice(idx,sum):
    global max_sum
    if idx == 11:
        if sum > max_sum:
            max_sum = sum
        return
    for i in range(11):
        if arr[idx][i] != 0 and visit[i] == 0:
            visit[i] = 1
            choice(idx+1,sum+arr[idx][i])
            visit[i] = 0

T = int(stdin.readline())
for tc in range(T):
    arr =[]
    for _ in range(11):
        arr.append(list(map(int,stdin.readline().split())))
    visit =[0]*11
    max_sum = 0
    choice(0,0)
    print(max_sum)


