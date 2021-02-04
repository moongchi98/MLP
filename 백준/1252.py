N= input().split()   
total = 0
for i in N:
    total += int(i,2)

result = ""
while total > 1:
    result += str(total % 2)
    total = total // 2
result += str(total)
result = result[::-1]
if result[0] == 0:
    result.pop(0)
    print(result)
else:
    print(result)

# 덕영님 풀이 천재만재?-> 이진법 덧셈 정의 활용
m, n = map(int, input().split())
add = list(str(m+n))
print(add)
reversed = []
result = []

for i in add[::-1]:
    reversed.append(int(i))
reversed.append(0)

for j in range (0,len(reversed)):
    #2진법 덧셈에서는 2가되면 앞자리로 1을 넘겨줘야한다는 속성이용
    if reversed[j] > 1:
        reversed[j+1] += 1
        reversed[j] -= 2
for i in reversed[::-1]:
    result.append(str(i))

if result[0] == '0':
    del result[0]
print (''.join(result))