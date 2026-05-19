"""
問題 C1：Maximum Range Sum
問題文

長さ N の整数列 A1,A2,…,AN が与えられます。
長さがちょうど K の連続する部分列を1つ選びます。
選んだ部分列の総和としてあり得る最大値を求めてください。

制約
1≤K≤N≤200000
1≤Ai≤1000
入力はすべて整数

入力
N K
A_1 A_2 ... A_N

出力
長さ K の連続部分列の総和の最大値を出力してください。
"""

N,K=map(int,input().split())
A=list(map(int,input().split()))

S=0
for i in range(K):
    S+=A[i]

max_sum=S

for j in range(1,N-K):
    S=S-A[j-1]+A[j+K-1]
    if S>max_sum:
        max_sum=S

print(S)
