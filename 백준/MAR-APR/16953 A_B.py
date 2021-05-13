a,b = map(int,input().split())

answer = 0
while a != b:
    if b < a:
        answer = -1
        break
    if b % 2 == 0 and b!=0:
        b = int(b/2)
        answer += 1
    elif str(b)[-1] == '1':
        b = str(b)[:-1]
        b = int(b)
        #이거를 그냥 b = int(b/10)으로 처리,,
        answer += 1
    else:
        answer = -1
        break
if answer != -1:
    answer += 1
print(answer)