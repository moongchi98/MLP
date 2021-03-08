from sys import stdin
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))
num.sort()
def comb(idx,sel):
    if idx==M:
        result.append(tuple(sel))
        return
    for i in range(N):
        if len(sel) == 0 or sel[-1] <=num[i]:
            comb(idx+1,sel+[num[i]])

result = []
visit= [0]*N
comb(0,[])
result = list(set(result))
result.sort()
for r in result:
    print(*r)
#반례
# 3 2
# 1 11 111
#실제 되야하는 출력
# 1 1
# 1 11
# 1 111
# 11 11
# 11 111
# 111 111
#코드로 나오는 출력
# 1 1
# 1 11
# 1 111
# 11 111
# 111 111