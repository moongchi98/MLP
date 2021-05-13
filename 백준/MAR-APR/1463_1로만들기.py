from sys import stdin
n = int(stdin.readline())
dp = [0]*(n+1)
for i in range(2,n+1):
    if not i % 2 and not i % 3:#공배수일경우에는 3가지 조건을 다 비교해야한다.
        dp[i] = min(dp[i-1]+1,dp[i//2]+1,dp[i//3]+1)
    elif not i % 3: #3으로 나누어진다면
        dp[i] = min(dp[i-1]+1,dp[i//3]+1) #1을 더해주는 거랑, 3을 나눠주는 횟수랑 비교
    elif not i % 2:
        dp[i] = min(dp[i-1]+1,dp[i//2]+1)
    else:
        dp[i] = dp[i-1] + 1
print(dp[n])
