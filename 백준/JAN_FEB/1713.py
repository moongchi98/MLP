N = int(input()) #사진틀 갯수
vote = int(input())
students = list(map(int,input().split()))
frame = []
recom =[] #frame에 들어가는 idx로 추천수를 지정한다

for i in range(vote):
    if students[i] in frame:
        for j in range(len(frame)):
            if students[i] == frame[j]:
                recom[j] += 1
    else:
        if len(frame) == N: #액자 차있는경우
            for j in range(N):
                if recom[j] == min(recom):
                    frame.pop(j)
                    recom.pop(j)
                    break

        #액자 비어있는 경우
        frame.append(students[i])
        recom.append(1)
            #결국 액자의 idx가 recom의 idx와 동일
frame.sort()
print(*frame)


