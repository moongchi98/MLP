def min_student():
    min_id = frame[0]
    cnt = 1
    min_s = []
    for i in range(len(votes)):
        if votes[i] != 0 and votes[i] < votes[min_id]:
            min_id = i #학생 번호
            min_s = [i]
            cnt = 1
        elif votes[i] != 0 and votes[i] == votes[min_id]:
            min_s.append(i)
            cnt += 1
    if cnt >= 2:
        #추가된지 오래된 애 부터 삭제
        v  = 0
        while v < len(vote):
            c = 0
            while c <len(min_s):
                if vote[v] == min_s[c]:
                    min_id = min_s[c]
                    return min_id
                    break
                else:
                    c += 1
            v += 1
    else:
        return min_id

N = int(input())
vote_cnt = int(input())
vote = list(map(int,input().split()))
max_s = max(vote)
#받은 득표수 표시하기 위해서
votes = [0]*(max_s+1)
frame = []
v = 0
while v < vote_cnt:
    if vote[v] not in frame:
        if len(frame) < N:
            frame.append(vote[v])
            votes[vote[v]] += 1
            v += 1
        elif len(frame) == N:
            #no는 학생 번호
            no = min_student()
            idx = frame.index(no)
            frame[idx] = vote[v]
            votes[no] = 0
            votes[vote[v]] += 1
            v += 1
            print(frame)
    else:
        votes[v] += 1


frame = list(set(frame))
frame.sort()
print(*frame)



