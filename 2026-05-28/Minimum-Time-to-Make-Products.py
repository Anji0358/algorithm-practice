N,K=map(int,input().split())
A=list(map(int,input().split()))

def calc(t):
    cnt=0

    for i in range(N):
        cnt+=A[i]*t
    return cnt>=K
    
ok=K
ng=0

while ok-ng>1:
    mid=(ok+ng)//2

    if calc(mid):
        ok=mid
    else:
        ng = mid

print(ok)

"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

def calc(t):
    cnt = 0

    for i in range(N):
        cnt += t // A[i]

        # K個以上作れることが分かったら早めに打ち切ってよい
        if cnt >= K:
            return True

    return cnt >= K

ng = 0
ok = min(A) * K

while ok - ng > 1:
    mid = (ok + ng) // 2

    if calc(mid):
        ok = mid
    else:
        ng = mid

print(ok)
"""