N=int(input())
A=list(map(int,input().split()))

dp=[0]*N

dp[0]=A[0]

if N==1:
    print(dp[0])
    exit()

dp[1]=max(dp[0],A[1])

for i in range(2, N):
    dp[i] = max(
        dp[i-1],  # 家 i を選ばない場合
        dp[i-2]+A[i]  # 家 i を選ぶ場合
    )

print(dp[N - 1])