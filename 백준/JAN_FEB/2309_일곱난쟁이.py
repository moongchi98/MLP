def dfs(idx,total,chosen):#뽑을 개수, 키의 합, 뽑은 애들
    global cnt #탈출 조건 설정하기 위해서,,
    if cnt == 1:
        return
    else:
        if idx == 2: #2명 뽑을거니까
            if total == 100:
                for t in trolls:
                    if t not in chosen:
                        print(t)
                cnt += 1
                return

            else:
                return

    for i in range(idx,9):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1,total - trolls[i],chosen + [trolls[i]])
            visited[i] = 0

cnt = 0
trolls =[]
visited =[0]*9
for _ in range(9):
    trolls.append(int(input()))
a = sum(trolls)
trolls.sort()
dfs(0,a,[])

#통과코드 - 반복문
# for i1 in range(8):
#     for i2 in range(i1+1,9):
#         if (trolls[i1]+trolls[i2] == total - 100):
#             result =[i1,i2]
#             break







