N = int(input())
students = []
new= []
for i in range(N):
    students.append([int(j) for j in input().split()])
# for i in range(N):
#     students.append(list(map(int,input().split(" "))))
print(students)



max_friend = -1
banjang = -1
for student_no in range(N):
    result =set()
    for friend in range(N):
        for grade in range(5):
            if students[student_no][grade] == students[friend][grade]:
                result.add(friend)               
    
    if len(result) > max_friend:
        banjang = student_no +1
        max_friend = len(result)
        

print(banjang)

        

# max_value = len(answer[0])
# dap= []
# for key,value in enumerate(answer):
#     if value == set():
#         continue
#     else:
#         if value > max_value:
#             max_value == value
#             dap = [key+1]
#         elif value == max_value:
#             dap += [key+1]
    

# max_value = len(answer[0])
# print(max_value)
# dap= []      
# for x in range(len(answer)):
#     if answer[x] > max_value:
#         max_value = len(answer[x])
#         dap = [x+1]
#     elif len(answer[x] == max_value):
#         dap += [x+1]
# print(min(dap))        

    
        

for idx in range(N-1):
    # print(idx,'i입니다')
    for j in range(5):
        # print(j,'j입니다')
        if students[idx][j] == students[idx+1][j]:
            # print(students[idx][j],students[idx+1][j])
            result[idx] = result.get(idx,0) + 1
            result[idx+1] = result.get(idx+1,0) + 1
            # print(result,'result입니다')
          
        else:
            continue


if result == {}:
    print(1)
else:
    max_value = max(result.values())
    answer =[]
    for key, value in result.items():
   
        if value > max_value:
            max_value = value
            answer = [key+1]
        elif value == max_value:
            answer += [key+1]
    print(min(answer))

