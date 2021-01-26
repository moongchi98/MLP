def solution(answers):
    cnt1, cnt2, cnt3 = 0, 0, 0
    #문제수에 맞게 이거 반복하는 걸 문제수에 딱 맞게 하는 방법은 없을까
    soopo1=[1, 2, 3, 4, 5]*(len(answers)+1)
    soopo2=[2, 1, 2, 3, 2, 4, 2, 5]*(len(answers)+1)
    soopo3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(len(answers)+1)

    for x in range(len(answers)):
            if answers[x] == soopo1[x]:
                cnt1 += 1
            if answers[x] == soopo2[x]:
                cnt2 += 1               
            if answers[x] == soopo3[x]:
                cnt3 += 1
    max_score = max(cnt1,cnt2,cnt3)
    print(max_score)
    result_list = [cnt1, cnt2, cnt3]
    answer = []
    for i in range(len(result_list)):
        if result_list[i] == max_score:
            answer += [i+1]
    return answer  

# def solution(answers):
#     soopo1=[1, 2, 3, 4, 5]
#     soopo2=[2, 1, 2, 3, 2, 4, 2, 5]
#     soopo3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     score = [0, 0, 0]
#     result = []
    
#     for idx, answer in enumerate(answers):
#         if answer == soopo1[idx % len(soopo1)]:
#             score[0] += 1 
#         if answer == soopo2[idx % len(soopo2)]:
#             score[1] += 1
#         if answer == soopo3[idx % len(soopo3)]:
#             score[2] += 1
    
#     for num, s in enumerate(score):
#         if s == max(score):
#             result.append(num+1)
#     return result
        
print(solution([1,3,2,4,2]))

