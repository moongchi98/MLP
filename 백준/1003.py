def fibo(n):
    cnt_0 = [1,0]
    cnt_1 = [0,1]
    for i in range (2,n+1):
        cnt_0.append(cnt_0[i-1]+cnt_0[i-2])
        cnt_1.append(cnt_1[i-1]+cnt_1[i-2])

    print(f'{cnt_0[n]} {cnt_1[n]}')

test_case = int(input())

for _ in range(test_case):
    fibo(int(input()))

