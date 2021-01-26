#내 풀이
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim' :
            return (f'김서방은 {i}에 있다')

#내장함수 index 사용
def solution(seoul):
    return (f'김서방은 {seoul.index('Kim')}에 있다')
