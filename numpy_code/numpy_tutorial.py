import numpy as np
import time
import sys

#For list memory occupied
l = range(1000)
print(type(l))
print (sys.getsizeof(5) * len(l))


#For numpy array

array = np.arange(1000)
print(array.size * array.itemsize)



#Now will check how numpy is faster then lisy 

SIZE = 1000000
l1 = range(SIZE)
l2 = range(SIZE)


#will add two list here
start_time = time.time()
result = [(a+b) for a,b in zip(l1,l2)]
print("time taken by list to add :", time.time() - start_time)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

#will see witg the numpy
start_time = time.time()
result = a1 + a2
print("time taken by numpy array is:",time.time() - start_time)


#With numpy we can create 2 Dimetion array 

'''
Documents :

ndim  : we can use to check property of the numpy array 
itemsize : it is use to check each element size 
dtype : it is to check for datatype of array
size :  it will give you total number of element
shape : it will provide infomation in dimetions
zeros : all element will initilize with 0 
linspace : this function generate array from given range
reshape  : we can reshape or existing array
  

''' 


a = np.array([12,3,4,5])
print(a)
print("dimmaintion :" , a.ndim) 

a = np.array([[1,2],[3,4],[5,6]])
print(a)
print("dimetion : ", a.ndim)

print("size of element:" , a.itemsize)
print("datatype :", a.dtype)

#How to change datatype of an array we can give extra argumetn call dtype while initilization

a = np.array([[1,2],[3,4],[5,6]] , dtype =np.float)
print("after changening dtype checkin dtype :" , a.dtype)
print("after changening dtype checkin iteamsize :" , a.itemsize)

#arange
a = np.arange(0,5)
print(a)
print(np.arange(0,5,2)) #3rd arg is step size 

a= np.linspace(0,5,10) #3rd arg is how many number you want to generate from 0,5

print(a)

a = np.array([[1,2],[3,4],[5,6]])

print(a.reshape(6,1))
print(a.reshape(2,3))
print(a.reshape(3,2))




