import numpy as np

counts = np.array([100, 250, 500, 750, 1000])

print("Gene counts:", counts)

log=np.round(np.log2(counts),2)
print("Log 2 values: ",log)

percent=np.round((counts/np.sum(counts))*100,1)
print("Gene percentages:",percent)