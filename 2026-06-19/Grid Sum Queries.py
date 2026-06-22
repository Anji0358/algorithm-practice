H,W,Q=map(int,input().split())

A=[[0]*(W+1) for _ in range(H+1)]

for i in range(W+1):
    A[i]=list(map(int,input().split()))

S=[[0]*(W+1) for _ in range(H+1) ]

for j in range(2,W+1):
    S[1][j]=S[1][j-1]+A[1][j]

for k in range(2,W+1):
    for k in range(1,H+1):
        S[i][k]=S[i][k-1]+S[i-1][k]-S[i-1][k-1]+A[i][k]

for l in range(Q):

    y1,x1,y2,x2=map(int,input().split())
    print(
        S[y2][x2]-S[y2][x1-1]-S[y1-1][x2]+S[y1-1][x1-1]
    )

"""
H, W, Q = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]

S = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] = (
            S[i][j + 1]
            + S[i + 1][j]
            - S[i][j]
            + A[i][j]
        )

for _ in range(Q):
    y1, x1, y2, x2 = map(int, input().split())
    print(
        S[y2][x2]
        - S[y1 - 1][x2]
        - S[y2][x1 - 1]
        + S[y1 - 1][x1 - 1]
    )
"""

