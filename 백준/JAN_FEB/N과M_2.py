#조합
def combi(idx,sel):
    if idx == M:
        print(*sel)

    for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                combi(idx+1,sel+[num[i]])
                #뽑았던 것은 다음 라운드에 안나오게 해주도록 i빼고 reset
                for j in range(i+1,N):
                    visit[j] = 0

from sys import stdin
N,M = map(int,stdin.readline().split())
num = [i for i in range(1,N+1)]
visit =[0]*(N)
combi(0,[])