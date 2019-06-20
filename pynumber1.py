import numpy as np

r=int(input("Enter no of row"))
c=int(input("Enter no of column"))

z=np.random.random((r,c))


f=open('numpy.txt','w')
f.write(str(z))
f.close()
