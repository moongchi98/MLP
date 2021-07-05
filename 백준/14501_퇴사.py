from sys import stdin
N = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]
D = [0]*N
for i in range(N):
    if (i+arr[i][0] -1 <N): #이 상담을 채택했을때 기간이 퇴사 전인지
        if D[i] < arr[i][1]:
            D[i] = arr[i][1]
    else:
        continue
    for j in range(i+1,N):
        if j - i > arr[i][0] -1 :
            if j + arr[j][0] -1 < N:
                if D[j] < D[i] + arr[j][1]:
                    D[j] =  D[i] + arr[j][1]
        else:
            continue
print(max(D))
