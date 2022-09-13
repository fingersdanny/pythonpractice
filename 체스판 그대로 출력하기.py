N, M = map(int, input().split())

chess = []
for i in range(N):
    chess.append([])
    for j in range(M):
        chess[i].append(0)

for i in range(N):
    a = input()
    for j in range(M):
        chess[i][j] = a[j]

for i in range(N):
    for j in range(M):
        print(chess[i][j], end = " ")
    print()