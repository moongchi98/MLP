from sys import stdin
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))
num.sort()
def comb(idx,sel):
    if idx==M:
        result.append(sel)
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            comb(idx+1,sel+str(num[i]))
            visit[i] = 0
visit = [0]*N
result = []
comb(0, "")
result = list(set(result))
result.sort()
for r in result:
    print(" ".join(r))

#not in으로 중복 점검 => 시간 초과
#str로 치환 경우에는 두자리 이상의 숫자가 하나하나로 처리
# ex)10000 => 1 0 0 0 0 