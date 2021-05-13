def dfs(idx,password,v,c):
    if idx == C:
        if len(password) == L:
            if v >= 1 and c >= 2:
                result.append(password)
                return
        return

    if visit[idx] == 0:
        visit[idx] = 1
        if arr[idx] in vowel:
            dfs(idx+1,password+arr[idx],v+1,c)
        else:
            dfs(idx + 1, password + arr[idx], v, c+1)
        visit[idx] = 0
        dfs(idx+1,password,v,c)

L,C = map(int,input().split())
arr = list(map(str,input().split()))
arr.sort()
result = []
vowel = ['a','e','i','o','u']
visit =[0]*(C)
dfs(0,"",0,0)
result = list(set(result))
result.sort()
for word in result:
    print(word)