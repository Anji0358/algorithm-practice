"""
問題 C2：Minimum Total Cost
問題文

N 個の商品があり、i 番目の商品の値段は Ai円です。
あなたはこの中からちょうど K 個の商品を買います。
支払う合計金額をできるだけ小さくするとき、その最小値を求めてください。

制約
1≤K≤N≤200000
1≤Ai≤10^9
入力はすべて整数

入力
N K
A_1 A_2 ... A_N

出力
ちょうど K 個の商品を買うときの合計金額の最小値を出力してください。
"""

N,K=map(int,input().split())
A=list(map(int,input().split()))

A.sort()

result=0

for i in range(K):
    result+=A[i]

print(result)
