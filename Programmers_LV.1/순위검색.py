#효율성 0점

def solution(info, query):
    applicants = []
    answer = [0]*len(query)
    for p in info:
        applicants.append(list(map(str,p.split())))
    for c in range(len(query)):
        condition = list(map(str,query[c].split(" and ")))
        print(condition)
        food,score = map(str,condition[3].split())
        lang,role,exp = condition[0],condition[1],condition[2]
        for person in applicants:
            point = 0
            if lang == '-' or lang == person[0]:
                point += 1
            if role == '-' or role == person[1]:
                point += 1
            if exp == '-' or exp == person[2]:
                point += 1
            if food == '-' or food == person[3]:
                point += 1
            if score == '-' or int(score) <= int(person[4]):
                point += 1
            if point == 5:
                answer[c] += 1
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))