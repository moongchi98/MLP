T =int(input())
cnt = 0
for _ in range(T):
    stack = []
    word = input()
    for alpa in word:
        if alpa not in stack:
            stack.append(alpa)
        else:
            if stack[-1] != alpa:
                break
    else:
        cnt += 1
print(cnt)
