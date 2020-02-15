#Cramers rule for solving linear equations

def cramer(m,w):
    x = np.zeros((len(m),1))
    determinant = np.linalg.det(m)
    for i in range(len(m)):
        m_1 = m.copy()
        m_1[:,i] = w[i,:]
        x[i] = (np.linalg.det(m_1)/determinant)
    return x
