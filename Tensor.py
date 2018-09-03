import numpy as np
x = np.array([[[1,4,7],
             [2,5,8],
             [2,6,9]],
            [[10,40,70],
               [20,50,80],
               [30,60,90]],
               [[100,400,700],
               [200,500,800],
               [300,600,800]]])
              
print(x)
print('A Tensor is of rank %d' %(x.ndim))
