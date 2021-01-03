import numpy as np
m1=np.random.uniform(0, 100, size=(8, 8))
m2=np.random.uniform(0, 100, size=(8, 8))
row=[0]*8
matrix_multi=[]
for n in range(0,8):
    matrix_multi.append(row)



for i in range(len(m1)):
    for j  in range(len(m2[0])):
        for p in range(len(m2)):
            matrix_multi[i][j]+=m1[i][p]* m2[p][j]

print(matrix_multi)








