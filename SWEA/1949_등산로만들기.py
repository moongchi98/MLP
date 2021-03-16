T = int(input())
for tc in range(1,T+1):
    N, K =map(int,input().split())
    arr = []
    max_h = 0
    max_list= []
    for i in range(N):
        tmp = list(map(int,input().split()))
        arr.append(tmp)
        for j in range(N):
            if tmp[j] > max_h:
                max_h = tmp[j]
                max_list =[(i,j)]
            elif tmp[j] == max_h:
                max_list.append((i,j))

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
