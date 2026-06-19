H,W,Q=map(int,input().split())

A=[[0]*(W+1) for _ in range(H)]

for i in range(1,W+1):
    A[i]=list(map(int,input().split()))

S=[[0]*(W+1) for _ in range(H+1) ]

for j in range(1,W+1):
    for k in range(1,H+1):
        S[i][k]=S[i][k-1]+A[i][k]


for l in range(Q):
    y1,x1,y2,x2=map(int,input().split())
    tmp=0

    for k in range(x1,x2):
        print(
            S[y2][x2]-S[y2][x1]-S[y1][x2]+S[y1][x1]
        )

