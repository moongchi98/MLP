def solution(s):
    stack = []
    for i in range (len(s)):
        #stack 비어있을때
        if len(stack) == 0:
            stack.append(s[i])
        #안비어있고, 가장 최근 원소가 같을때 삭제
        elif stack[-1] == s[i]:
            stack.pop()
        #다르면 그냥 추가 
        else:
            stack.append(s[i])
            
    if len(stack) == 0 :
        return 1
    else:
        return 0
        



s='baabaa'
print(solution(s))
print(solution('cdcd'))

# s=list(s)
# print(s)

# for i in range (0,len(s)-2):
 #     print(i)
       
#     if s[i] == s[i+1]:
#         s.pop(i)
#         print(s)
#         s.pop(i)
#         print(s)
#         i=0
#     else:
#         continue
        
# if s == []:
#     return 1
# else:
#     return 0

#2번째시도
# i = 0 
#     while i <= (len(s)-2):
#         if s[i] == s[i+1]:
#             s = s.replace(s[i],"",2)
#             i = 0
#         else:
#             i += 1 
#     if len(s) == 0:
#         return 1
#     else:
#         return 0