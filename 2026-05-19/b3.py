"""
問題 B1：Range Sum
問題文
N 個の整数 A_1, A_2, ..., A_N と、整数 L, R が与えられます。
A_i のうち、L 以上 R 以下であるものだけを合計してください。

制約
1 ≤ N ≤ 100
1 ≤ L ≤ R ≤ 1000
1 ≤ A_i ≤ 1000
入力はすべて整数

入力
N L R
A_1 A_2 ... A_N

出力
条件を満たす A_i の合計を出力してください。
"""

N,L,R=map(int,input().split())
A=list(int,input().split())

total=0

for i in range(0,N):
    if L<=A[i]<=R:tatal+=A[i]

print(total)

