N,Q=map(int,input().split())
A=list(int,input().split())
L=[0]*Q
R=[0]*Q

for i in range(Q):
    l,r=map(int,input().split())
    L[i]=l
    R[i]=r

result=[0]*N
result[0]=A[0]

for i in range(N):
    result[i]=result[i-1]+A[i]

for j in range(Q):
    print(result[R[j]]-result[L[j-1]])

    """
    N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N + 1)

for i in range(N):
    S[i + 1] = S[i] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L - 1])
    """