def solution(n,s,a,b,fares):
    arr = [[0]*(n+1) for _ in range(n+1)]
    visit = [0]*(n+1)
    stack = []
    for fare in fares:
        d1 = fare[0]
        d2 = fare[1]
        arr[d1][d2] = fare[2]
        arr[d2][d1] = fare[2]
        if d1 == s:
            stack.append(d2)
    while stack:
        p = stack.pop()
        if visit[p] == 0:
            visit[p] = 1
            for near in arr[p]:
                if visit[near] != 1:
                    stack.pop(near)


