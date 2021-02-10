import sys
scores=[]
for m in range(5):
    scores.append(sum(list(map(int,sys.stdin.readline().split()))))
max_p = max(scores)
idx = scores.index(max_p) + 1
print(f'{idx} {max_p}')

result = []
for participant in scores:
    for i in range (1,4):
        participant[i] += participant[i-1]
    participant = participant[-1]
    result.append(participant)

max_id = max_value = 0
for key,value in enumerate(result):
    if value > max_value:
        max_value = value
        max_id = key 
print(f'{max_id+1} {max_value}')


    

        
