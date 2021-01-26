# k = int(input())
# N = 3**k
def star_func(N):
    result =[]
    if N == 3:
        block=("*"*3+"\n"+"* *"+"\n"+"*"*3+"\n")
        return block

    if N > 3:
        N = N // 3
        square = (" "*N+"\n")*N
        for j in range(3):
            result.append(star_func(N))
        for i in range (len(result)):
            print(result[i],end="")
                


(star_func(9))
print(1 % 5)