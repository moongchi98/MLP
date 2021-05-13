from sys import stdin
T = int(stdin.readline())
for tc in range(1,T+1):
    N = int(stdin.readline())
    candidates = []
    for _ in range(N):
        (x,y) = map(int,stdin.readline().split())
        candidates.append((x,y))
    #버블정렬
    candidates.sort()

    # [(1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]
    #
    # [(1, 4), (2, 5), (3, 6), (4, 2), (5, 7), (6, 1), (7, 3)]

    #두번째 전형의 값을 앞의 애들이랑 비교해서 작으면 탈락
    total = N
    min_value = candidates[0][1]
    for i in range(1,N):
        if candidates[i][1] > min_value:
            total -= 1
        else:
            min_value = candidates[i][1]

    print(total)