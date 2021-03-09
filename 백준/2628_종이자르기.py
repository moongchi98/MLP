def lotto(pick_num):
    results = {'1등':0, '2등':0, '3등':0, '4등':0, '5등':0, '꽝':0}
    lucky= [7,9,22,27,37,42]
    bonus = 34
    cnt = 0
    for p in pick_num:
        for luck in lucky:
            if p == luck:
                cnt += 1
    if cnt == 6:
        results['1등'] += 1
    elif cnt == 5 and bonus in pick_num:
        results['2등'] += 1
    elif cnt == 5:
        results['3등'] += 1
    elif cnt == 4:
        results['4등'] += 1
    elif cnt == 3:
        results['5등'] += 1
    else:
        results['꽝'] += 1
    return results

print(lotto([7,9,22,27,37,45]))