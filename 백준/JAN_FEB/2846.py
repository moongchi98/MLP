N = int(input())
roads = list(map(int,input().split()))
max_uphill = 0
uphill = 0
for i in range(1,N):
    if roads[i] > roads[i-1]:
        uphill += (roads[i] - roads[i-1])
        if uphill >max_uphill:
            max_uphill = uphill
        
    else:
        uphill = 0
        
print(max_uphill)


