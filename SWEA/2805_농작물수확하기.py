def above_center(center):
  r = 0
  #다음줄의 c의 범위가 달라지도록 만들기
  start = center
  benefit = 0
  end = start + 1
  while r < center+1:
    c = start
    while start<=c<end:
      benefit += vegi[r][c]
      c += 1
    start -= 1
    end += 1
    r += 1
  return benefit

def under_center(center):
  r = center + 1
  #다음줄의 c의 범위가 달라지도록 만들기
  start = 1 
  benefit = 0
  end = N-1
  while r < N:
    c = start
    while start<=c<end:
      benefit += vegi[r][c]
      c += 1
    start += 1
    end -= 1
    r += 1
  return benefit

T = int(input())
for tc in range(1,T+1):
  N = int(input())
  vegi = []
  for _ in range(N):
    vegi.append(list(map(int,input())))
  center = int(N//2)
  total = above_center(center) + under_center(center)
  print(f'#{tc} {total}')