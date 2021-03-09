N, K = map(int,input().split())
countries = []
for _ in range(N):
    countries.append(list(map(int,input().split())))
countries.sort(key=lambda x : (x[1],x[2],x[3]),reverse=True)
#key를 통해서 정렬기준을 설정해준다. 즉 각 원소의 1,2,3인덱스를 기준으로
#정렬 이때 뒤에 reberse=True를 하면 내림차순 정렬
for i in range(N):
    if countries[i][0] == K:
        idx = i
for j in range(N):
    if countries[idx][1:] == countries[j][1:]:
        print(j+1)
        break

    


