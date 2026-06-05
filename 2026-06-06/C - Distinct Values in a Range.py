import sys

input =sys.stdin.readline

N,Q=map(int,input().split())
A=list(map(int,input().split()))

bit=[0]*(N+1)

def add(i,x):
    i+=1
    while i <=N:
        bit[i]+=x
        i+=i & -i
    
def prefix_sum(i):
    i+=1
    res=0
    while i>0:
        res+=bit[i]
        i-=i & -i
    return res

def range_sum(l,r):
    return prefix_sum(r)-prefix_sum(l-1) if l>0 else prefix_sum(r)

queries=[[] for _ in range(N)]

for qi in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    queries[R].append((L, qi))

last = {}
ans = [0] * Q

for i, x in enumerate(A):
    if x in last:
        add(last[x], -1)

    add(i, 1)
    last[x] = i

    for L, qi in queries[i]:
        ans[qi] = range_sum(L, i)

print(*ans, sep="\n")


