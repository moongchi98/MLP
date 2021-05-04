def powerset(N,arr):
    global candidate
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                print(arr[j],end="")

candidate ={}
def solution(orders, course):
    global candidate
    # dictinoary 형태로..?
    for order in orders:
        powerset(len(order),order)
    return candidate

orders =["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
solution(orders,course)
print(candidate)
