N=int(input())
total = 0

left = N % 5
mok = N // 5

while mok > -1:
    if N % 5 == 0:
        total = N //5
        print(total)
        break

    M = N - (mok)*5
    
    if M % 3 == 0:
        total = (mok)+(M//3)
        print(total)
        break
    else:
        mok -= 1
        left += 5
        total = 0
if total == 0:
    print(-1)

# while True:
#     if N % 5 == 0:
#         total += N //5 
#         print(total)
#         break
#     else:
#         N = N - 3
#         total += 1
    
#     if N < 0:
#         print(-1)
#         break

# 반례 19
# if N % 5 == 1:
#     X = N//5 -1
#     N = N - 5*X
#     Y = N // 3
#     total = X + Y
#     print(total)

# elif N % 5 == 3:
#     X = N // 5
#     Y =1
#     total = X + Y
#     print(total)

# elif N % 5 == 0:
#     total = N // 5
#     print(total)

# elif N % 3 == 0:
#     total = N // 3
#     print(total)

# else:
#     print(-1)
