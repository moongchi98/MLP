N = int(input())
# test_cases = []
test_cases= [list(map(str,input().split("X"))) for i in range(N)]

for test_case in test_cases:
    score = 0
    for answer in test_case:
        if answer != '':
            for i in range(1,len(answer)+1):
                score += i
    print(score)

