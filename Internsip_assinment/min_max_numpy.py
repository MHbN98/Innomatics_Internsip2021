import numpy as np

n,m=map(int,input().split())

li=[list(map(int,input().split())) for i in range(n)]

ar=np.array(li)

print(max(np.min(ar,axis=1)))