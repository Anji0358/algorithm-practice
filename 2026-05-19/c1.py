"""
問題 C1：Pair Sum Count
問題文

N 個の整数 A1,A2,…,ANと整数 K が与えられます。
1≤i<j≤N を満たす組 (i,j) のうち、
Ai+Aj=K
となる組の個数を求めてください。

制約
2≤N≤100
1≤K≤200
1≤Ai≤100
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
    for j in range(0,N):
        if A[i]+A[j]==K:cnt+=1

print(cnt)