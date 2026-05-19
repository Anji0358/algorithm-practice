"""
問題 C1：Three Sum Count

問題文
N 個の整数 A_1, A_2, ..., A_N と整数 K が与えられます。
1 ≤ i < j < k ≤ N を満たす組 (i, j, k) のうち、
A_i + A_j + A_k = K
となる組の個数を求めてください。

制約
3 ≤ N ≤ 50
1 ≤ K ≤ 300
1 ≤ A_i ≤ 100
入力はすべて整数

入力
N K
A_1 A_2 ... A_N

出力
条件を満たす組の個数を出力してください。
"""

N,K=map(int,input().split())
A=list(map(int,input().split()))

cnt=0
for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i]+A[i]+A[j]==k:
                cnt+=1

print(cnt)