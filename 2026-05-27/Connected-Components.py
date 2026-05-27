from collections import deque

N,M=map(int,input().split())

G=[[] for _ in range(M)]

for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

visited=[False]*N

q=deque(0)
cnt=0
while q:
    
    v=q.popleft()
    for nv in G[v]:
        if visited[v]!=False:
            continue

        q.append(nv)
        visited[nv]=True
    cnt+=1

"""
from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

visited = [False] * N

cnt = 0

for start in range(N):
    if visited[start]:
        continue

    cnt += 1

    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()

        for nv in G[v]:
            if visited[nv]:
                continue

            visited[nv] = True
            q.append(nv)

print(cnt)
"""
