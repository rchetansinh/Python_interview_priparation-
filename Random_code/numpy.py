import numpy as np

arr = np.array([1, 3, 2, 4, 5])


#5,4,2,3,1
print(arr.argsort()[-3:][::-1])



print(arr.argsort())
#print(arr.argsort()[-3:][::-1])
