N = int(input())
wanted=list(map(int,input().split()))
taken=[]
cnt = 0
for want in wanted:
    if want not in taken:
        taken.append(want)
    else:
        cnt += 1
        continue

print(cnt)