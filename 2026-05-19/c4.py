"""
問題 C2：Prefix Range Sum

問題文

N 個の整数 A_1, A_2, ..., A_N が与えられます。
続いて Q 個の質問が与えられます。
各質問では整数 L, R が与えられるので、A_L + A_{L+1} + ... + A_R を出力してください。

制約
1 ≤ N ≤ 200000
1 ≤ Q ≤ 200000
1 ≤ A_i ≤ 1000
1 ≤ L ≤ R ≤ N
入力はすべて整数

入力
N Q
A_1 A_2 ... A_N
L_1 R_1
L_2 R_2
...
L_Q R_Q

出力
Q 行出力してください。
i 行目には、i 番目の質問の答えを出力してください。
"""

N,Q=map(int,input().split())
A=list(map(int,input().split()))

total=0
for i in range(0,Q):
    L,R=map(int,input().split())
    for j in range(L-1,R):
        total+=A[j]
    
    print(total)
    total=0


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