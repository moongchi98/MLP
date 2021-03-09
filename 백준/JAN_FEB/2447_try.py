def star_func(N):
    if N == 3:
        b3 = [["*","*","*"], ["*"," ","*"], ["*","*","*"]]
        for b in b3:
            for x in range(len(b)):
                print(b[x],end="")
            print()
    else:
        N = N // 3
        square = (" "*3+"\n")*3   
        a3 = [[star_func(N),star_func(N),star_func(N)],\
            [star_func(N),square,star_func(N)],[star_func(N),star_func(N),star_func(N)]]
        for a in a3:
            for y in range(len(a)):
                print(a[y],end="")
            print()
star_func(9)