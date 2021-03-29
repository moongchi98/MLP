N = int(input())
time = list(map(int,input().split()))
    #버블 정렬로 작은 순서대로 정렬하기
for j in range(N-1,0,-1):
    for i in range(0,j):
        if time[i] > time[i+1]:
            time[i],time[i+1] = time[i+1], time[i]
    #누적합 구하기
for i in range(1,N):
    time [i] += time[i-1]
print(sum(time))