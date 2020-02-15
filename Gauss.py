import numpy as np


def gauss_elimination(A,B):
    n = len(B)
    x = np.zeros(n,float)

    #Elimination
    for k in range(n-1):
        #Protection if zeros are on diagonal
        if A[k,k] == 0:
            for i in range(k+1, n):
            	if A[i,k] != 0:
	                A[[k,i]] = A[[i,k]]
	                B[[k,i]] = B[[i,k]]
	                break #Brake when the rows are changed
        #Setting values to 0 at the diagonal
        for i in range(k+1,n):
            wspl = A[k,k] / A[i,k]
            for j in range(k,n):
                A[i,j] = A[k,j] - (A[i,j] * wspl)
            B[i] = B[k] - (B[i]*wspl)

    #Backward solution
    x[n-1] = B[n-1] / A[n-1,n-1]
    for i in range(n-2,-1,-1):
        sums = 0
        for j in range(i+1,n):
            sums = sums + A[i,j] * x[j]
        x[i] = (B[i] - sums) / A[i,i]

    return x