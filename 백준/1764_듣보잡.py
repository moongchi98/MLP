#이진탐색
def binary_search(start,end,target):
    while start <= end:
        middle = int((start+end)/2)
        if bodo[middle] == target:
            return True
        if bodo[middle] > target:
            return(binary_search(start,middle-1,target))
        elif bodo[middle] < target:
            return(binary_search(middle+1,end,target))
    return False

N, M = map(int,input().split())
ddeut = sorted([input() for i in range(N)])
bodo = sorted([input() for i in range(M)])
cnt = 0
result = []
for x in ddeut:
    start = 0
    end = M-1
    if binary_search(start,end,x) :
        cnt += 1
        result.append(x)
result.sort()
print(cnt)
for x in result:
    print(x)
#통과코드
# result = sorted(list(ddeut&bodo))
# print(len(result))
# for i in result:
#     print(i)






# #시간초과
# cnt = 0
# result = []
# for name in ddeut:
#     if name in bodo:
#         cnt += 1
#         result.append(name)
# print(cnt)
# result.sort()
# for x in result:
#     print(x)
