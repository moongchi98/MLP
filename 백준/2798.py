# N,M = map(int,input().split(" "))
# Numbers = list(map(int,input().split(' ')))

result = []
for i in range(N):
    for j in range (i+1, N):
        for z in range(j+1 , N):
            total = Numbers[i]+Numbers[j]+Numbers[z]
            if total <= M:
                result.append(total)
print(max(result))
#역순으로 하면 더 빠르징않을까? 근데 계속 오류
# def Black(N,M,Numbers):
#     Numbers.sort()
#     Numbers = Numbers[::-1]
#     print(Numbers)
#     result =set()
#     for i in range(N-2):
#         for j in range (i+1, N-1):
#             for z in range(j+1 , N):
#                 total = Numbers[i]+Numbers[j]+Numbers[z]
#                 if total <= M:
#                     result.add(total)
#                     break
#                 elif total == M:
#                     return total
#     print(max([*result]))
# N,M = map(int,input().split(" "))
# Numbers = list(map(int,input().split(' ')))
# Black(N,M,Numbers)

#1번째시도
