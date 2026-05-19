"""
問題文
N 人の点数 A
A1,A2,...,ANが与えられます。
点数が 60 点以上の人を合格者とします。
合格者が1人以上いる場合、合格者の平均点を小数点以下を切り捨てて出力してください。
合格者が1人もいない場合は 0 を出力してください。
"""

N=int(input())
A=list(map(int,input().split()))
flag=False
for i in range(0,N):
    if A[i]>=60:
        flag=True
        break

if flag:print(sum(A)//N)
else:print(0)