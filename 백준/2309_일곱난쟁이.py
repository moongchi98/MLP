def dfs(cnt): #cnt가 고른 개수
    total = 140
    if cnt == 2:
        for idx in next:
            total -= trolls[idx]
        if total == 100:
            return next

        else:
            total = 140
            return


    for i in range(9):
        if not visited[i]:
            visited[i] = 1
            next.append(i)

            dfs(cnt+1)
            next.pop()

            for j in range(i+1,9):
                visited[j] = 0
#
# next = []
trolls =[]
# visited =[0]*9
for _ in range(9):
    trolls.append(int(input()))
total = sum(trolls)
for i1 in range(8):
    for i2 in range(i1+1,9):
        if (trolls[i1]+trolls[i2] == total - 100):
            result =[i1,i2]
            break


for x in result:
    trolls[x] = 0
trolls.sort()
for t in trolls:
    if t != 0:
        print(t)








