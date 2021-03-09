from sys import stdin
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))
num.sort()
def comb(idx,sel):
    if idx==M:
        print(*sel)
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            comb(idx+1,sel+[num[i]])
            #앞에서 나왔던 숫자가 나오면 안될때는 i빼고 reset
            for j in range(i+1,N):
                visit[j] = 0
visit = [0]*N
comb(0, [])