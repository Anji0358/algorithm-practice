N=int(input())

rel=[]
A=[-1]*N

for i in range(N):
    a,b=map(int,input().split())
    rel.append((a,b))

rel.sort()

for a,b in rel:
    if a==-1:
        A[a]=1
    elif a==1:
        A[b]==0
    else:
        continue

print(sum(A))

"""
N, M = map(int, input().split())

parent = [i for i in range(N)]
size = [1] * N

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union(a, b)

roots = set()

for i in range(N):
    roots.add(find(i))

print(len(roots))
"""