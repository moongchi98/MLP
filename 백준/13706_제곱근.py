def binary_search(start,end):
    N = end
    while True:
        middle = (start+end)//2 #여기서 int((start+end)/2)로 구하면 시간 초과 발생한다.. 왜지?
        if middle ** 2 == N:
            return middle
        if middle ** 2 < N:
            start = middle
        elif middle ** 2 > N:
            end = middle
N = int(input())
print(binary_search(1,N))
