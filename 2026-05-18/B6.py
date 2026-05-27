N=list(int,map().split())

cnt=0
sum=0

for i in range(0,N):
    if N[i]>=60:
        cnt+=1
        sum+=N[i]

print(cnt)
print(sum)

# not sum ,but ans
