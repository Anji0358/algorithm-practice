n=int(input())
a=list(map(int,input().split()))

cur=a[1]+a[1]+1
for i in range(1,n-1):
    for j in range(i+1,n):
        cur=max(cur,a[i]+a[j]+j)

print(cur)

"""
n = int(input())
a = list(map(int, input().split()))

best_left = a[0] - 0
ans = -10**30

for j in range(1, n):
    ans = max(ans, best_left + a[j] + j)
    best_left = max(best_left, a[j] - j)

print(ans)
"""