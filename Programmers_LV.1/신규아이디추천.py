def solution(new_id):
    #1번
    new_id = list(map(str,new_id.lower()))
    arr= ""
    #2번
    for i in range(len(new_id)):
        if 48<=ord(new_id[i])<=57 or 97<=ord(new_id[i])<=122:
            arr += (new_id[i])
        else:
            if new_id[i] != '-' and new_id[i] != '_' and new_id[i] != '.':
                continue
            else:
                arr += new_id[i]
    #3번
    while '..' in arr:
        arr = arr.replace('..','.')
    #4번 => slicing으로 접근
    if len(arr) > 1:
        if arr[0] == '.':
            arr = arr[1:]
        if arr[-1] == '.':
            arr = arr[:-1]
    elif len(arr) == 1 and arr[0] == '.':
        arr = ""

    #5번
    if len(arr) == 0:
        arr += "a"
    #6번
    if len(arr) >= 16:
        arr = arr[:15]
        if arr[14] == '.':
            arr = arr[:14]
    #7번
    if len(arr) <=2:
        while len(arr) < 3:
            arr += arr[-1]
            if len(arr) == 3:
                break
    return arr

print(solution(".1."))
