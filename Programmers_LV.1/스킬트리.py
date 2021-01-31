                  
def solution(skill, skill_trees):
    cnt = 0
    result = []
    for skills in skill_trees:
        real_skill = []
        for x in skills:
            if x in skill:
                real_skill.append(x)
        real_skill = "".join(real_skill)
        if real_skill == skill[:len(real_skill)]:
            cnt += 1
        else:
            continue
    return cnt

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))

    #pop으로 비교, for else문 사용   
    # cnt = 0
    # for skills in skill_trees:
    #     skill_list = list(skill)
    #     for x in skills:
    #         if x in skill:
    #             if x != skill_list.pop(0):
    #                 break
    #     else:
    #         cnt +=1 
    # return cnt



#for-else문 사용, 내 풀이 좀 수정
# cnt = 0
#     result = []
#     for skills in skill_trees:
#         real_skill = []
#         for x in skills:
#             if x in skill:
#                 real_skill.append(x)
#         for i in range(len(real_skill)):
#             if real_skill[i] != skill[i]:
#                 break
#         else:
#             cnt += 1
#     return cnt
            

