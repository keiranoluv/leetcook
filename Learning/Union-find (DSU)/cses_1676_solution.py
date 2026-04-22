n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))
    1
def find(x):
    if fa[x]!=x:
        fa[x] = find(fa[x])
    return fa[x]

fa = list(range(n+1))
size = [1]*(n+1)
fa[0]=-1
components = n
max_size = 1

def union(x,y):
    global components # Declare components as global
    global max_size
    x = find(x)
    y = find(y)
    if (x==y):
        return
    if (size[x]<size[y]):
        x,y = y,x
    fa[y]=x
    size[x]+=size[y]
    max_size = max(max_size,size[x])
    components-=1

for edge in edges:
    union(edge[0], edge[1])
    print(components, max_size)