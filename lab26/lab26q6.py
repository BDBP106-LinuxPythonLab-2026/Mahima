import numpy as np
rg=np.random.default_rng()
a=rg.random(9)
a=a.reshape(3,3)
print("Original matrix:\n",a)

np.set_printoptions(precision=3)
print("Print options:\n",a)