import numpy as np
n=int(input())
a = np.array([input().split() for _ in range(n)],int)
b = np.array([input().split() for _ in range(n)],int)
m = np.dot(a,b)
print (m)