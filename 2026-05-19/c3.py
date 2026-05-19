"""
問題 C1：Different Pair Count

問題文
N 個の整数 A_1, A_2, ..., A_N が与えられます。
1 ≤ i < j ≤ N を満たす組 (i, j) のうち、A_i と A_j が異なる組の個数を求めてください。

制約
2 ≤ N ≤ 200
1 ≤ A_i ≤ 100
入力はすべて整数

入力
N
A_1 A_2 ... A_N

出力
条件を満たす組の個数を出力してください。
"""
N=int(input())
A=list(map(int,input().split()))

cnt=0

for i in range(0,N):
    for j in range(i+1,N):
        if A[i]!=A[j]:
            cnt+=1

print(cnt)