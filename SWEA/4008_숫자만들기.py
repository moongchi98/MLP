#memory limit exceed..
import itertools
def check(a,b,o):
    if o =='+':
        return a+b
    elif o =='-':
        return a-b
    elif o =='*':
        return a*b
    elif o == '/':
        return int(a/b)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tmp = list(map(int,input().split()))
    #연산자 저장
    operators = ['+','-','*','/']
    o_list = []
    for i in range(4):
        for j in range(tmp[i]):
            o_list.append(operators[i])
    #수식의 숫자들
    numbers = list(map(int,input().split()))
    #연산자 배치 방법의 수
    result = list(itertools.permutations(o_list,len(o_list)))
    cases = []
    i = 0
    while i < len(result):
        stack = []
        j = k = 0
        while j<N:
            stack.append(numbers[j])
            if j == N:
                break
            if k == len(result[0]):
                break
            else:
                stack.append(result[i][k])
            j += 1
            k += 1
        cases.append(stack)
        i += 1

    #각 case들의 결과 구하기
    answer= set()
    c = 0
    while c < len(cases):
        tmp_1 = (cases[0][0])
        case = cases[c]
        idx = 1
        while idx <=len(case)-2:
            total = check(tmp_1,case[idx+1],case[idx])
            tmp_1 = total
            idx += 2
        answer.add(total)
        c += 1
    real_answer = max(answer)-min(answer)

    print(f'#{tc} {real_answer}')



