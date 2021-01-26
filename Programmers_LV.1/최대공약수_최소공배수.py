def solution(n, m):
    answer = []
    div = [x for x in range (1,n+1) if n % x== 0 and m % x == 0]
    answer.append(div[-1])
    max = div[-1] * (n // div[-1]) * (m // div[-1])
    answer.append(max)
    return answer

