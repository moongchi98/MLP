Room_no = input()
result = {}
for num in Room_no:
    if num not in result:
        result[num]=Room_no.count(num)
    else:
        continue


if (result.get('6', 0) + result.get('9', 0)) % 2 :
    result['mean'] = (result.get('6', 0) + result.get('9', 0))//2 + 1
    result.pop('9',"")
    result.pop('6',"")
else:
    result['mean'] = (result.get('6', 0) + result.get('9', 0))//2
    result.pop('9',"")
    result.pop('6',"")
print(max(result.values()))
    