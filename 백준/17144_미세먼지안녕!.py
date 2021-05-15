from sys import stdin
from collections import deque
def spread():
    dusty_room = deque() #미세먼지가 있는방들
    spread_room = deque()
    for r in range(R):
        for c in range(C):
            if room[r][c] != -1 and room[r][c] != 0:
                dusty_room.append((r,c))
    while dusty_room:
        for j in range(len(dusty_room)):
            r,c = dusty_room[j]
            cnt = 0 #퍼트린 방의 개수
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<R and 0<=nc<C:
                    if room[nr][nc] != -1:
                        dust = room[r][c] // 5
                        spread_room.append((nr,nc,dust))
                        cnt += 1
            spread_room.append((r,c,-(room[r][c]//5*cnt)))
        return spread_room

def air_cleaner():
    moving = []
    idx = 0
    i,j = cleaner[idx]
    nr,nc = i,j+1
    moving.append((nr,nc,0))
    #위에있을때
    while True:
        if nr == i and nc != j:
            while 0<nc < C-1:
                moving.append((nr,nc+1,room[nr][nc]))
                nc += 1
            if nc == C-1:
                moving.append((nr-1,nc,room[nr][nc]))
                nr -= 1
        elif 0<nr<i and nc== C-1:
            while nr > 0:
                moving.append((nr-1,nc,room[nr][nc]))
                nr -= 1
        elif nr == 0:
            while nc > 0:
                moving.append((nr,nc-1,room[nr][nc]))
                nc -= 1
            if nc == 0:
                moving.append((nr+1,nc,room[nr][nc]))
                nr += 1
        elif 0<nr<i and nc == 0:
            while nr < i-1:
                moving.append((nr+1,nc,room[nr][nc]))
                nr += 1
            if nr == i-1:
                nr += 1
        elif nr == i and nc == j:
            break
    #아래 있은 녀석
    idx = 1
    i,j = cleaner[idx]
    nr,nc = i,j+1
    moving.append((nr,nc,0))
    while True:
        if nr == i and nc != j:
            while 0<nc < C-1:
                moving.append((nr,nc+1,room[nr][nc]))
                nc += 1
            if nc == C-1:
                moving.append((nr+1,nc,room[nr][nc]))
                nr += 1
        elif i<nr<R-1 and nc== C-1:
            while nr < R-1:
                moving.append((nr+1,nc,room[nr][nc]))
                nr += 1
        elif nr == R-1:
            while nc > 0:
                moving.append((nr,nc-1,room[nr][nc]))
                nc -= 1
            if nc == 0:
                moving.append((nr-1,nc,room[nr][nc]))
                nr -= 1
        elif i<nr<R-1 and nc == 0:
            while nr > i+1:
                moving.append((nr-1,nc,room[nr][nc]))
                nr -= 1
            if nr == i + 1:
                nr -= 1
        elif nr == i and nc == j:
            break

    return moving

R,C,T = map(int,stdin.readline().split())
room = [list(map(int,stdin.readline().split())) for _ in range(R)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
time = 0
cleaner = [] #공기 청정기의 위치치
for r in range(R):
    for c in range(C):
        if room[r][c] == -1:
            cleaner.append((r,c))
while time < T:
    arr = spread()
    for p in arr:
        i,j,a = p
        room[i][j] += a
    moving = air_cleaner()
    for n in moving:
        nr,nc,na = n
        room[nr][nc] = na
    time += 1
answer = sum(sum(room,[]))
answer += 2
print(answer)
