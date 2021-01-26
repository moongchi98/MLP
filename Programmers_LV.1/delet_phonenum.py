#내 풀이
def solution(phone_number):
    answer=""
    for i in range (len(phone_number)):
        if i < (len(phone_number)-4):
            answer += "*"
        else:
            answer += phone_number[i]
    return answer

#문자열 곱셈 활용
def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]
    