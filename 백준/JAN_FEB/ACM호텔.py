T = int(input())
case = [input().split(" ") for i in range(T)]
# print(case)
for trial_case in case:

    result = ""
    H = int(trial_case[0])
    N = int(trial_case[2])
    floor = N % H
    if floor == 0:
        floor = H
        room_no = N // H
    else:
        room_no = (N//H)+1

    if room_no < 10:
        result += str(floor) + "0" + str(room_no)
    else:
        result += str(floor)+ str(room_no)
    print(result)
    floor*100+room_NO