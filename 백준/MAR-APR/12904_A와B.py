S = input()
T = input()

while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
    if len(S) > len(T):
        result = 0
        break
    elif len(S) == len(T) and S != T:
        result = 0
        break
    elif S == T:
        result = 1
        break
print(result)

