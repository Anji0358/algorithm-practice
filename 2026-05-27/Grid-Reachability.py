from collections import deque

H,W=map(int,input().split())
c=[]
sy=sx=-1
gy=gx=-1

for i in range(H):
    row=input()
    c.append(row)

    for j in range(W):
        if row[j]=="S":
            sy,sx=i,j
        elif row[j]=="G":
            gy,gx=i,j

dy=[1,-1,0,0]
dx=[0,0,-1,1]
dist=[[-1]*W for _ in range(H)]

q=deque()
q.append((sy,sx))
dist[sy][sx]=0

while q:
    y,x=q.popleft()

    for i in range(4):
        ny=y+dy[i]
        nx=y+dx[i]

        if c[ny][nx]=="G":
            print("Yes")

        if ny<0 or ny>=H or nx<0 or nx>=W:
            continue

        if c[ny][nx]=="#":
            continue

        if dist[ny][nx]!=-1:
            continue

        dist[ny][nx]=dist[y][x]+1
        q.append((ny,nx)) 

print("No")

