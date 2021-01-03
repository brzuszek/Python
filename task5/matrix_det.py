import random
import numpy as np
def determinant_fast(A):

    n = len(A)
    AM = A

    for diag in range(n):
        for p in range(diag+1,n):
            if AM[diag][diag] == 0:
                AM[diag][diag] == 1.0e-18
            crScaler = AM[p][diag] / AM[diag][diag]
            for j in range(n):
                AM[p][j] = AM[p][j] - crScaler * AM[diag][j]

    product = 1.0
    for i in range(n):
        product *= AM[i][i]

    return product


num=random.randint(2,10)
arr1 = np.random.uniform(0, 100, size=(num, num))

print(determinant_fast(arr1))
print(np.linalg.det(arr1))
