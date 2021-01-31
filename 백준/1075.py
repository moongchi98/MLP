N = input()
F= int(input())
N = N[-len(N):-2:1] +"00"

if int(N) % F == 0:
    new_end = N
else:
    new_end = str((int(N) // F + 1) * F)

print(new_end[-2:])

# #원래시도
# N = input()
# F= int(input())
# N = N[-len(N):-2:1] +"00"

# new_end = str((int(N) // F + 1) * F)

# print(new_end[-2:])