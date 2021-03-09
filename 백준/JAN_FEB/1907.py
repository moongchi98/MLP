from itertools import product
equation=input().split("=")
equation += equation[0].split("+")
equation.pop(0)
equation.reverse()
#A+B->C의 반응식에서, 내 equation은 [B,A,C] 순서로 담겨있다

result =[]

for element in equation:
    atom={}
    #딕서너리에 각 반응물 '원소':개수로 설정
    for i in range(len(element)):
        if element[i].isdigit():
            #만약 숫자라면 앞에문자개수가 숫자만큼이다.
            #'원소':1일때, -1해주고 곱해주면 에러가 생기고, 
            #중복을 방지하기 위해 1*숫자 -1 로 설정해줬다.
            #숫자 나오기 전에, 문자가 카운트됬으므로 -1해줘야함
            atom[element[i-1]]=atom.get(element[i-1])+(1* int(element[i]))-1
        else:
            atom[element[i]] = atom.get(element[i],0) + 1
    result.append(atom)

#중복순열->(1,1,1) 부터 (10,10,10)
answer=[]
for x in product(range(1,11),range(1,11),range(1,11)):
    X2=x[0]
    X1=x[1]
    X3=x[2]

    left_C= X1*result[1].get('C',0)+X2*result[0].get('C',0)
    left_O= X1*result[1].get('O',0)+X2*result[0].get('O',0)
    left_H= X1*result[1].get('H',0)+X2*result[0].get('H',0)

    right_C= X3*result[2].get('C',0)
    right_O= X3*result[2].get('O',0)
    right_H= X3*result[2].get('H',0)
    
    if left_C-right_C == 0 and left_H - right_H ==0 and left_O-right_O ==0:
        answer+=[(X1, X2, X3)]
#(X1이 가장 작은놈)이 답이되고->X1동일시 X2작은놈
answer.sort()
for j in answer[0]:
    print(j, end=" ")
