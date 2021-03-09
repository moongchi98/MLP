N = int(input())
scores=[]
cnt = 0
for n in range(N):
    scores.append(int(input()))

for i in range(N-1,0,-1):

    if scores[i] <= scores[i-1]:
        cnt += (scores[i-1] - scores[i] +1)
        scores[i-1] = scores[i] -1

    else:
        continue
print(cnt)

# 시간초과
# N = int(input())
# scores=[]
# cnt = 0
# for n in range(N):
#     scores.append(int(input()))

# for i in range(N-1,0,-1):

#     if scores[i] - scores[i-1] != 1:
#         while scores[i] - scores[i-1] != 1:
#             scores[i-1] -= 1
#             cnt += 1

#     else:
#         continue
# print(cnt)
