N=int(input())
#비치는 모습 input 받기 위해서
goul = []
#한 줄당 imput으로 받고, 그 한 줄이 goul의 한 개의 요소
for i in range(N):
    goul.append(input())
K=int(input())

if K == 1:
    print('\n'.join(goul))
if K == 2:
    #좌우반전
    for j in goul:
        #안의 각줄을 역으로해서 print
        print(j[::-1])  
if K == 3:
    #상하반전
    #reverse는 원본을 변형
    goul.reverse()
    #전체를 reverse하고 줄바꿈으로 구분해서 출력
    print("\n".join(goul))