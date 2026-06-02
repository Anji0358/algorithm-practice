N,K=map(int,input().split())
X=list(map(int,input().split()))

def calc(d):
    for i in range(0,N-1):
        for j in range(i+1,N):
            if d>abs(X[i],X[j]):
                return True
    
    return False

## dを与えたときに存在するかで調べる

ok=0
ng=max(X)-min(X)

while -ok+ng>0:
    mid=(ok+ng)//2

    if calc(mid):
        ok=mid
    else:
        ng=mid

print(ok)

"""
N, K = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

def calc(d):
    count = 1
    last = X[0]

    for i in range(1, N):
        if X[i] - last >= d:
            count += 1
            last = X[i]

    return count >= K

ok = 0
ng = max(X) - min(X) + 1

while ng - ok > 1:
    mid = (ok + ng) // 2

    if calc(mid):
        ok = mid
    else:
        ng = mid

print(ok)
"""
