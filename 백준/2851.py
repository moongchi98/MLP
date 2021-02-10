mushroom = []
for k in range (10):
    mushroom.append(int(input()))

# 그냥
result = 0
for i in mushroom:
    result += i
    if result >= 100:
        if abs(result-100) <= abs(100-(result-i)):
            break
        else:
            result -= i
            break
print(result)

# 누적합
idx = 0
while True:
    for i in range (1,10):
        mushroom[i] += mushroom[i-1]
        if mushroom[i] > 100:
            idx = i
            break
    if abs(mushroom[idx]-100) < abs(mushroom[idx-1]-100):
        print(mushroom[idx])
        break
    elif abs(mushroom[idx]-100) == abs(mushroom[idx-1]-100):
        print(mushroom[idx])
        break
    else:
        print(mushroom[idx-1])
        break