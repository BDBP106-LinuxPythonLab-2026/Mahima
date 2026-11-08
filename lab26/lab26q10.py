import numpy as np
time=np.arange(0,121,20)
population=100*2**(time/20)
print(population)
print("The final population is",population[len(time)-1]/population[0],"times larger than the initial population.")
print("Time at which population larger the 1000:",time[population>1000])