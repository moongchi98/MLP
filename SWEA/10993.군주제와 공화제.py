T = int(input())

for tc in range(1, T+1):
    city = []
    N = int(input())
    for n in range(N):
        city.append(list(map(int,input().split())))
    print(city)

    result =""
    # i번째 도시가 j번째 도시에 미치는 영향
    for i in range(N):
        threat = []
        max_id = ""
        max_power = 0
        for j in range (N):
            print(i,'i입니다',j,'j입니다')
            if j != i:
                xi, yi, si = city[i][0], city[i][1], city[i][2]
                xj, yj, sj = city[j][0], city[j][1], city[j][2]

                radius = ((xj-xi)**2+(yj-yi)**2)
                # i가 j국가에게 미치는 영향 이게 sj보다 크다면 위협이 된다.
                power = sj / radius
                print(power,j)
                if power > si:
                    threat.append(str(j))
                    print(threat,power)
                    if power > max_power:
                        max_power = power
                        max_id = str(j)
                    elif power == max_power:
                        max_id += str(j)
                else:
                    continue
        print(max_id)
        if len(threat) == 0:
            result += 'K'
        elif len(max_id) >= 2:
            result += "D"
        elif len(max_id) == 1:
            result += str(max_id)
    print(f'#{tc}'+(" ").join(result))



