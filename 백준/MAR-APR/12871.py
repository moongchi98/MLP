from math import gcd #최소 공배수
def lcm(x):
    pattern = int((len(s) / x) * (len(t) / x) * x)
    S = pattern / len(s)
    T = pattern /  len(t)
    S,T = int(S), int(T)
    return S,T

s = input()
t = input()
#abcdef ab의 경우 1로 출력
if len(s) == len(t):
    if s == t:
        answer =1
    else:
        answer = 0
else:
    x = gcd(len(s),len(t))
    S,T = lcm(x)
    fs = s * S
    ft = t *T
    if fs == ft:
        answer = 1
    else:
        answer = 0
print(answer)