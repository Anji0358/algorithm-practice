n=int(input())
a=list(map(int,input().split()))

##0~i max

best=[0]*n
cur=a[0]
best[0]=cur

for i in range(0,n):
    cur=max(a[i],cur+a[i])
    best[i]=max(cur+a[i],best[i-1])


worst=[0]*n
cur=a[0]
worst[0]=cur

for i in range(1,n):
    cur=min(a[i],cur+a[i])
    worst[i]=min(worst[i-1],cur+a[i])

result=max(best)-min(worst)
print(result)

"""
n = int(input())
a = list(map(int, input().split()))

max_cur = a[0]
max_sum = a[0]

min_cur = a[0]
min_sum = a[0]

for i in range(1, n):
    max_cur = max(a[i], max_cur + a[i])
    max_sum = max(max_sum, max_cur)

    min_cur = min(a[i], min_cur + a[i])
    min_sum = min(min_sum, min_cur)

print(max_sum - min_sum)
"""
