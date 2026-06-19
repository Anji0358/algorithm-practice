N = int(input())

A = [0] * N
B = [0] * N
C = [0] * N

for i in range(N):
    a, b, c = map(int, input().split())
    A[i] = a
    B[i] = b
    C[i] = c

dp = [[0] * 3 for _ in range(N)]

dp[0][0] = A[0]
dp[0][1] = B[0]
dp[0][2] = C[0]

for i in range(1, N):
    dp[i][0] = A[i] + max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = B[i] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = C[i] + max(dp[i - 1][0], dp[i - 1][1])

print(max(dp[N - 1]))