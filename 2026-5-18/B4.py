N=int(input())
S=input()

cnt=0
pre=""
cur=""
for i in range(0,N):
    cur=S[i]
    if(pre==cur):cnt+=1
    pre=cur



"""
for i in range(N - 1):
    if S[i] == S[i + 1]:
        cnt += 1
"""