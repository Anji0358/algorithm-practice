from collections import deque

N,M=map(int,input().split())

G=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
    
color=[0]*N

for v in range(N):
    
    if color[v]==0:
        continue

    q=deque(v)
    color[v]=1

    for nv in G[v]:
        if color[nv]==0:
            continue

        if color[nv]==color[v]:
            print("No")
            exit()

        color[nv]=-1*G[v]
        q.append(nv)

print("Yes")

"""
from collections import deque

# 0: 未訪問
# 1: 色1
# -1: 色2

N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

color = [0] * N

for start in range(N):
    if color[start] != 0:
        continue

    color[start] = 1
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()

        for nv in G[v]:
            if color[nv] == 0:
                color[nv] = -color[v]
                q.append(nv)
            else:
                if color[nv] == color[v]:
                    print("No")
                    exit()

print("Yes")
"""
