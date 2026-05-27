N=int(input())
C=list(map(int,input().split()))

dp=[0]*N

dp[0]=0
dp[1]=C[1]

for i in range(2,N):
    dp[i]=min(
        dp[i-2]+C[i],
        dp[i-1]+C[i]
    )

print(dp[N-1])