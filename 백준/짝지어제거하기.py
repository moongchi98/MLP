def solution(s):
    s=list(s)
    print(s)

    for i in range (0,len(s)-2):
        print(i)
       
        if s[i] == s[i+1]:
            s.pop(i)
            print(s)
            s.pop(i)
            print(s)
            i=0
        else:
            continue
        
    if s == []:
        return 1
    else:
        return 0

s='baabaa'
solution(s)