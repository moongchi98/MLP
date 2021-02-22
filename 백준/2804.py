def same(A,B):
    for r in range(len(A)):
        for c in range(len(B)):
            if A[r] == B[c]:
                common = (r,c)
                return common
                break

A,B=input().split()
#점으로 채운 기본 행렬 생성하기
cross_word = []
for i in range(len(B)):
    sentence = []
    for j in range(len(A)):
        sentence.append('.')
    cross_word.append(sentence)
r, c = same(A,B)[0],same(A,B)[1]
cross_word[c] = list(A)
for j in range(len(B)):
    cross_word[j][r] = B[j]
#출력
for cross in cross_word:
    for word in cross:
        print(word,end="")
    print()
