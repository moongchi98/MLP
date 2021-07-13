from sys import stdin
def clean(r,c,d):
    global cleaned
    if arr[r][c] == 0:
        arr[r][c] = 2 # 청소 했다
        cleaned += 1
    dr =[(-1,0),(0,1),(1,0),(0,-1)]
    # 왼쪽 방향 부터 비어있는 곳 확인
    for i in range(4):
        nd = (d+3) % 4
        nr = r + dr[nd][0]
        nc = c + dr[nd][1]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 0 :
            clean(nr,nc,nd)
            return
        d = nd #현재에서 왼쪽 방향으로
    br =[(1,0),(0,-1),(-1,0),(0,1)] #후진 좌표
    nx = r + br[d][0]
    ny = c + br[d][1]
    if 0<=nx<N and 0<=ny<M and arr[nx][ny] != 1:
        clean(nx,ny,d)
    else:
        return
N,M = map(int,stdin.readline().split())
sr,sc,d = map(int,stdin.readline().split()) #로봇 출발 좌표, 방향
arr = [list(map(int,stdin.readline().split())) for _ in range(N)]
cleaned = 0 #청소한 방의 개수
clean(sr,sc,d)
print(cleaned)

from collections import deque
# def cleaning(r,c,d,turn): # 1번 항목 청소겸 자리 탐색
#     global cleaned,ans
#     if not visited[r][c]:
#         cleaned += 1 # 현재위치 청소
#         visited[r][c] = 1
#     if turn == 3:
#         ans.append((r, c, d))
#         return
#     next = False
#     #1. 왼쪽 방향 탐색
#     if d == 0: #북쪽을 바라볼때
#         next = (r,c-1)
#         next_d = 3
#     elif d == 1: #동쪽
#         next = (r-1,c)
#         next_d = 0
#     elif d == 2:
#         next = (r,c+1)
#         next_d = 1
#     elif d == 3:
#         next = (r+1,c)
#         next_d = 2
#
#     if next: #이동할 칸이 잇는 경우
#         if 0<=next[0]<N and 0<=next[1]<M and arr[next[0]][next[1]] != 1 and not visited[next[0]][next[1]]:
#             ans.append((next[0],next[1],next_d,0))
#             return
#             # cleaning(next[0],next[1],next_d,0)
#         else:
#             ans.append((r,c,next_d,turn+1))
#             return
#             # cleaning(r,c,next_d,turn+1)
#
#
# # 왼쪽 없을 경우 탐색
# def whirl(r,c,direction):
#     global ans
#     #후진하기
#     if direction == 0 :
#         next = (r+1,c)
#         behind = r + 1
#     elif direction == 1:
#         next = (r,c-1)
#         behind = c- 1
#     elif direction == 2:
#         next = (r-1,c)
#         behind = r -1
#     elif direction == 3:
#         next = (r,c+1)
#         behind = c + 1
#     if 0<=next[0]<N and 0<=next[1]<M and arr[next[0]][next[1]] != 1 :
#         ans.append((next[0],next[1],direction,0))
#         return
#         # cleaning(next[0],next[1],direction)
#     elif behind < 0 or behind >=N or behind >= M or arr[next[0]][next[1]] == 1:
#         ans = []
#         return


