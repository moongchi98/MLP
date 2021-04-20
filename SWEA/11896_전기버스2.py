#전기버스 동건 형님의 코드,..
for tc in range(1, 1 + int(input())):
    N, *M = map(int, input().split()) # *M을 하면 첫번째 값만 n에 저장하고ㅓ, 나머지는 m에
    # dp
    dp = [-1] + [100] * (len(M))
    for i in range(len(M)): #정류장 개수만큼
        for j in range(M[i]): #최대 이동 거리 이내에서
            if i + j + 1 > len(M): continue #범위넘어가면
            dp[i + j + 1] = min(dp[i] + 1,dp[i + j + 1])
            #내 추측에 dp[i] + 1은 i번째 정류소에서 충전을 하고 온다는 뜻, dp[i+j+1]은 기존의값
            print(dp[i+j+1],i+j+1)
    print("#{} {}".format(tc, dp[-1]))
