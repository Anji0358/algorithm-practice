"""
問題文
長さ N の文字列 S が与えられます。
同じ文字が連続している部分のうち、最も長い長さを求めてください。
制約
1≤N≤100
S は英小文字からなる長さ N の文字列

入力
N
S

出力
同じ文字が連続している部分の最大長を出力してください。
"""

N=int(input())
S=input()

max=0
crr=0
tmp=S[0]

for i in range(0,N):
    if(tmp==S[i]):
        crr+=1
        if(crr>=max):max=crr
    else:
        crr=0
        tmp=S[i]

print(max)


