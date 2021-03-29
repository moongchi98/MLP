def counting(arr):
    count = [0] * (N)
    for i in range(N - 1, -1, -1):
        if arr[i] > N:
            return -1
        else:
            count[arr[i]] += 1
    return count

def check(count):
    global cnt,no_1
    for j in range(1,len(count)):
        if count[j-1] < count[j]:
            return -1
        elif count[j] == 2:
            cnt += 1
        elif count[j] == 1:
            no_1 = 1
            return 1
    return 1

N = int(input())
arr = list(map(int,input().split()))
cnt = no_1 =  0
if counting(arr) != -1:
    count = counting(arr)
    check(count)
    if check(count) == 1:
        answer = (2**cnt) * (2**no_1)
        print(answer)
    else:
        answer = 0
        print(answer)




