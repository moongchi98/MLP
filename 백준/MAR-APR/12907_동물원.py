#카운트 정렬에 표시
C = [0]*41 #숫자가 40까지 가능하기 때문에 범위를 41까지로 해줘야 한다. 
N = int(input())
arr = list(map(int,input().split()))
for num in arr:
    C[num] += 1
prev_cnt = 2
answer = 1
for cnt in C:
    if cnt > prev_cnt:
        answer = -1
        break
    prev_cnt = cnt
if answer == -1:
    print(0)
else:
    if 1 in C:
        result = 2**(C.count(2)+1)
    else:
        result = 2**(C.count(2))
    print(result)





