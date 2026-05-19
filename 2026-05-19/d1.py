"""
問題 D1：Can Reach

問題文
N 個のマスが横一列に並んでいます。
左から i 番目のマスには整数 A_i が書かれています。
あなたは最初、マス 1 にいます。
マス i にいるとき、マス i + A_i に移動できます。
マス N に到達できるなら Yes、到達できないなら No を出力してください。
ただし、移動先が N を超える場合、その移動はできません。

制約
2 ≤ N ≤ 200000
1 ≤ A_i ≤ N
入力はすべて整数

入力
N
A_1 A_2 ... A_N

出力
マス N に到達できるなら Yes、到達できないなら No を出力してください。
"""

N=int(input())
A=list(map(int,input().split()))

i=1
if N==1:print("Yes")

while(N>i):
    i=i+A[i]
    if i==N:
        print("Yes")

print("No")

    