T= int(input())
numbers = []
for num in range(T):
    numbers.append(list(map(int,input().split())))
    

for test_case in numbers:
    result = []
    for i in range (2, test_case[0]):
        if test_case[0] % i ==0:
            result.append(i)
            
    # print(sum(result))
    if test_case[1] == sum(result):
        print('yes')
    else:
        print('no')
