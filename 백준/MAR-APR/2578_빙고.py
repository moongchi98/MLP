from sys import stdin
from collections import deque
def bingo_find(i,j):
    total = 0
    #가로 찾기
    for r in range(5):
        if sum(visit[r][0:5]) == 5:
            total += 1

    #세로 찾기
    for c in range(5):
        col = 0
        for r in range(5):
            if visit[r][c] == 1:
                col += 1
            if col == 5:
                total += 1

    #대각선 찾기
    right_down = left_down = 0
    for i in range(5):
        if visit[i][i] == 1:
            right_down += 1
        if visit[i][4-i] == 1:
            left_down += 1
    #전체 빙고 개수
    if left_down == 5:
        total += 1
    elif right_down == 5:
        total += 1
    return total
positions = [0]*(26) #빙고판의 숫자별 위치 저장
for r in range(5):
    tmp = list(map(int, stdin.readline().split()))
    for c in range(5):
        positions[tmp[c]] = ((r,c))
numbers =[] #사회자의 숫자들

for _ in range(5): #1차원 list로 받아오기
    numbers += list(map(int,stdin.readline().split()))
numbers = deque(numbers)

cnt = 0 #사회자가 부른 숫자의 개수
visit =[[0]*5 for _ in range(5)] #숫자 불려지면 체크 용도
while numbers:
    num = numbers.popleft()
    cnt +=1
    i,j = positions[num]
    visit[i][j] = 1
    if bingo_find(i,j) >= 3:
        print(cnt)
        break