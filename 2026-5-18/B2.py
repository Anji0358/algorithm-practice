N=int(input())

cnt=0

for i in range(1,N+1):
    if i%3 or i%5 :cnt+=1

print(cnt)