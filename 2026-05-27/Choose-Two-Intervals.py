"""
間違えた
N=int(input())
A=list(map(int,input().split()))

def cal(A,l,r):
    result=0

    for i in range(l,r):
        result+=A[i]

    return result

max=0
tmp=0
for l1 in range(0,N):
    for r1 in range(l1+1,N):
        for l2 in range(r1+1,N):
            for r2 in range(l2,N):
                tmp=cal(A,l1,r1)+cal(A,l2,r2)
                if(tmp>max):max=tmp

print(max)
"""

N=int(input())
A=list(map(int,input().split()))

INF=10**30

left_best=[0]*N
right_best=[0]*N

cur=A[0]
left_best=A[0]

for i in range(1,N):
    cur=max(A[i],cur+A[i])
    left_best[i]=max(left_best[i-1],cur)

cur=A[N-1]
right_best=A[N-1]

for i in range(N-2,-1,-1):
    cur=max(A[i],cur+A[i])
    right_best[i]=max(cur,right_best[i+1])

ans=-INF

for i in range(N - 1):
    ans = max(ans, left_best[i] + right_best[i + 1])

print(ans)


