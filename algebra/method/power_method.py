import numpy as np
#1.26.2버전
print(np.__version__)

A = np.array([[6,5],[1,2]])

xk = np.array([0,1])

for k in range(1,7):
    Axk = A@xk
    mk = Axk.flat[np.abs(Axk).argmax()]
    print('xk : ',xk,'Axk : ',Axk,'mk : ',mk)
    xk = np.divide(Axk,mk)