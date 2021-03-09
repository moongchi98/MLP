# #내풀이
x=int(input())
y=int(input())
answer=[]
def three_digi(x, y):
    while y > 0 :
        result = x * (y % 10)
        print(result)
        answer.append(result)
        y = (y // 10)
    return answer

three_digi(x, y)
total = 0
for i in range (len(answer)):
    total += answer[i]*(10**i)
print(total)

#간단풀이
x = int(input())
y = input()[::-1] #아예 string으로 받아서 index 사용,역으로
result= []
print(y)
def multip(x,y):
    for i in y:
        gob = x * int(i)
        result.append(gob)
    return result          
total = 0
multip(x, y)
for j in range (len(result)):
    total += result[j]*(10**j)
print(total)


