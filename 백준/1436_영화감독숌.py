N = int(input())

cnt = 1
start = 666
while cnt != N:
    start += 1
    s = str(start)
    if '666' in s:
        cnt += 1
    if cnt == N:
        break
print(start)
