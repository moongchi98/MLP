#dp연습,,,
def solution(triangle):
    def dfs(r, c, total):
        if r == N:
            return total

    if 0 <= r + 1 < N:
        dfs(r + 1, c, total + triangle[r][c])
        dfs(r + 1, c + 1, total + triangle[r][c])

    N = len(triangle)
    max_total = 0
    if dfs(0, 0, 0, N) > max_total:
        max_total = total
    return max_total
