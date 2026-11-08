import numpy as np
A=[1,0,0,0]
T=[0,1,0,0]
G=[0,0,1,0]
C=[0,0,0,1]
seq="GATTACA"
seq=list(seq)
seq=",".join(seq)
print(seq)
seq_arr=np.array(eval(seq))
print(seq_arr)