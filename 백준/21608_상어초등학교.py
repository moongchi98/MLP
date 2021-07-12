from sys import stdin

#자리배치 알고리즘
def seat(person,like): #좋아하는 학생들 list를 받음
    d = [(-1,0),(1,0),(0,1),(0,-1)]
    max_cnt = -1
    candidates= []
    for r in range(N):
        for c in range(N):
            cnt = 0 #좋아하는 학생의 수
            if not used[r][c]:
                for dr,dc in d:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<N and 0<=nc<N:
                        #최애학생이 있는지 확인
                        if used[nr][nc] in like:
                            cnt += 1

                if cnt > max_cnt :
                    max_cnt = cnt
                    candidates = [(r,c)]
                elif cnt == max_cnt:
                    candidates.append((r,c))
    # 2번째 단계, 빈 공간 많은 애들
    if len(candidates) == 1: #하나만 있다면 걔네들로 자리지정
        x,y = candidates[0][0],candidates[0][1]
        used[x][y] = person #그 사람 지정해주기
        return (x,y)
    else:
        max_blank = -1 #인접한 빈 자리의 개수
        new_candidates = []
        for r,c in candidates:
            blank = 0
            for dr,dc in d:
                nr = r + dr
                nc = c + dc
                if 0<=nr<N and 0<=nc<N and not used[nr][nc]: #자리가 차있지 않다면,
                    blank += 1
            if blank > max_blank:
                max_blank = blank
                new_candidates = [(r,c)]
            elif blank == max_blank:
                new_candidates.append((r,c))
    # 3번째 단계 비교용
    if len(new_candidates) == 1:
        x, y = new_candidates[0][0], new_candidates[0][1]
        used[x][y] = person  # 그 사람 지정해주기
        return (x,y)
    else:
        min_r = 1000
        next = []
        for p in new_candidates:
            if p[0] < min_r:
                min_r = p[0]
                next = [(p[0],p[1])]
            elif p[0] == min_r :
                next.append((p[0],p[1]))
        if len(next) == 1:
            nx,ny = next[0][0],next[0][1]
            used[nx][ny] = person
            return (nx,ny)
        else:
            last_c = last_r = 1000
            for n in next:
                if n[1] < last_c:
                    last_c = n[1]
                    last_r = n[0]
            used[last_r][last_c] = person
            return (last_r,last_c)

#만족도조사
def preference(person,position,like):
    global total
    cnt = 0
    r,c = position[0], position[1]
    d = [(-1,0),(1,0),(0,1),(0,-1)]
    for dr,dc in d:
        nr = r+ dr
        nc = c + dc
        if 0<=nr<N and 0<=nc<N and used[nr][nc] in like:
                cnt += 1
    if cnt == 1:
        total += 1
    elif cnt == 2:
        total += 10
    elif cnt == 3:
        total += 100
    elif cnt == 4:
        total += 1000

N = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(N**2)]
used = [[0]*N for _ in range(N)]
total = 0 #전체 만족도
for human in arr:
    person = human[0]
    like = set(human[1:])
    seat(person,like)
    # print(used,person)
for r in range(N):
    for c in range(N):
        for p in arr:
            if p[0] == used[r][c] :
                like = p[1:]
                position = (r,c)
                person = p[0]
                preference(person,position,like)
print(total)
