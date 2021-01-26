def solution(n,a,b):
    answer = 0
    #a랑 b가 같아지면 겨룬다는 이야기
    while a != b:
        #우선 다르니까 1라운드 추가
        answer += 1
        #다음라운드에 부여 받을 번호
        #처음에는 짝, 홀 나누었지만 상관없이 +1한 후 나누어주면 된다.
        a = (a+1) // 2
        b = (b+1)// 2
    return answer

    