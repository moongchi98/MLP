problem = 0

while True:
    sentence = input()

    if sentence == '고무오리 디버깅 시작':
        continue
    
    if sentence == '문제':
        problem += 1
    
    if sentence == '고무오리' and problem == 0:
        problem += 2
    elif sentence =='고무오리' and problem != 0:
        problem -= 1

    if sentence == '고무오리 디버깅 끝':
        break

if problem == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')