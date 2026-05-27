
N,K=map(int,input().split())
A=list(map(int,input().split()))

cnt=0

for i in range(0,len(A)):
    if A[i]<=K:cnt+=1

print(cnt)

"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for x in A:
    if x <= K:
        ans += x

print(ans)
"""
