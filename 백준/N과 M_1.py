from sys import stdin
def combi(idx,sel):
    if idx == M:
        print(*sel)
    else:
        #for문이 있어야 모든 numbers가 나온다
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                combi(idx+1,sel+[numbers[i]])
                visit[i] = 0

#순열
N,M = map(int,stdin.readline().split())
numbers = [i for i in range(1,N+1)]
visit =[0]*(N)
combi(0,[])

