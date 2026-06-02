N=int(input())

jobs=[]
for i in range(N):
    s,t=map(int,input().split())
    jobs.append((t,s))

jobs.sort()

cur=0
ans=0

for t,s in jobs:
    if s>= cur:
        ans+=1
        cur=t

print(ans)