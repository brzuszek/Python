
import numpy as np
m1=np.random.uniform(0, 100, size=(128, 128))
m2=np.random.uniform(0, 100, size=(128, 128))

matrix_sum=[]


for i in range(len(m1)):
    new=[]
    for j in range(len(m1[0])):
        new.append(m1[i][j]+m2[i][j])
    matrix_sum.append(new)








