#격자 원래대로 변경 함수
def point_change(c,r):
    c,r = r,c
    r = 100 - r
    return r,c                                  

#색종이가 깔릴 격자 만들기
palette = []
for _ in range(101):
    palette.append([100]*101)

def check_cnt(idx):
    cnt = 0
    for row in palette:
        for col in row:
            if col == idx:
                cnt += 1
    return cnt

#input
N = int(input())
color_paper = []
for _ in range(N):
    color_paper.append(list(map(int,input().split())))
for x in range(N):
    print(x,'x')
    p1 = (point_change(color_paper[x][0],color_paper[x][1]))[0]
    p2 = (point_change(color_paper[x][0],color_paper[x][1]))[1]
    w = color_paper[x][2]
    h = color_paper[x][3]
    for i in range(h):
        nr = p1 - i
        for j in range(w):
            nc = p2 + j
            print((nr,nc),'nc')
            palette[nr][nc] = x
for x in range(N):
    print(check_cnt(x))
  