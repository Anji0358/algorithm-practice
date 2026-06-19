N=int(input())
A=list(map(int,input().split()))

dp=[0]*N

dp[0]=A[0]

if N==1:
    print(dp[0])
    exit()

dp[1]=dp[0]+A[1]

if N==2:
    print(dp[1])
    exit()

dp[2]=max(dp[0]+A[2],dp[1],A[1]+A[2])

for i in range(3,N):
    dp[i]=max(
        dp[i-3]+A[i-1]+A[i],
        dp[i-2]+A[i],
        dp[i-1]
    )

print(dp[N-1])