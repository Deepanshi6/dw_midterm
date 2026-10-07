import numpy as np

a=np.array([[10,20,30],[40,50,60]])

mean_c=np.average(a,axis=0)
print("mean of each column :",mean_c)

print("output of a[a>25] :",a[a>25])