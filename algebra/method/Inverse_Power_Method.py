import numpy as np
#1.26.2버전
print(np.__version__)

A = np.array([[10,-8,-4],
              [-8,13,4],
              [-4,5,4]])
a = 3.3
xk = np.array([1,1,1])


print('a : 3.3')
for k in range(1,7):
    yk = np.linalg.solve(A-a*np.eye(3),xk)
    mk = yk.flat[np.abs(yk).argmax()]
    vk = a + 1/mk
    print('xk : ',xk,'yk : ',yk,'mk : ',mk, 'vk : ',vk)
    #print(xk)
    xk = np.divide(yk,mk)

A = np.array([[10,-8,-4],
              [-8,13,4],
              [-4,5,4]])
a = 1.9
xk = np.array([1,1,1])


print('\n\na : 1.9')
for k in range(1,7):
    yk = np.linalg.solve(A-a*np.eye(3),xk)
    mk = yk.flat[np.abs(yk).argmax()]
    vk = a + 1/mk
    print('xk : ',xk,'yk : ',yk,'mk : ',mk, 'vk : ',vk)
    #print(xk)
    xk = np.divide(yk,mk)